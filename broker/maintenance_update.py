import cglogging as cgl
import lambda_accessor
import Message

logger_Class = cgl.cglogging()
logger = logger_Class.setup_logging()


def handler_request(request):
    message = Message.Message()
    camp_request = {}
    camp_details = {"aircraftDetails": []}
    rusada_request = {}
    for aircraft in request["request"]["aircraftDetails"]:
        if aircraft["maintenanceProvider"].upper() == "CAMP".upper():
            camp_details["aircraftDetails"].append(get_camp_items(aircraft)["aircraftDetails"])

        if aircraft["maintenanceProvider"].upper() == "RUSADA":
            logger.debug(request)
            rusada_request = get_camp_items(request)

    camp_request = build_camp_request(request, camp_details)

    return_code, return_message, camp_response = lambda_accessor.lambda_accessor.call_camp(camp_request)
    logger.debug("done calling camp")
    return return_code, return_message, camp_response


def get_camp_items(request):
    items_list = {"items": []}
    for item in request["items"]:
        position = None
        modelName = None
        partNo = None
        if "position" in item and item["position"] != "None":
            position = "NO. " + str(item["position"])

        if "modelName" in item and item["modelName"] != "None":
            modelName = item["modelName"]

        if "partNo" in item and item["partNo"] != "None":
            partNo = item["partNo"]

        items_list["items"].append({
            "profileType": item["profileType"],
            "serial": item["serial"],
            "position": position,
            "unit": item["unit"],
            "lastReportedValue": item["lastReportedValue"],
            "lastReportedDate": item["lastReportedDate"],
            "modelName": modelName,
            "partNo": partNo
        })

    return {
        "aircraftDetails": {
            "secretName": request["secretName"],
            "keyPrefix": request["keyPrefix"],
            "orderId": request["orderId"],
            "orderItemId": request["orderItemId"],
            "modelName": request["modelName"],
            "regNo": request["regNo"],
            "serial": request["serial"],
            "items": items_list["items"]
        }
    }


def build_camp_request(request, camp_details):
    return {
        "context": request["context"],
        "commonParms": {
            "action": "updateTotals",
            "view": "CAMP",
            "version": "1.0.0",
            "transactionId": "PETERG ORDER"
        },
        "request": {
            "supplierId": request["request"]["supplierId"],
            "aircraftDetails": camp_details["aircraftDetails"]
        }

    }
