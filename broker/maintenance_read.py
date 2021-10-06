import cglogging as cgl
from lambda_accessor import lambda_accessor
import Message

logger_Class = cgl.cglogging()
logger = logger_Class.setup_logging()


def handler_request(request):
    message = Message.Message()
    camp_aircraft_details = {"aircraftDetails": []}
    rusada_aircraft_details = {"aircraftDetails": []}
    # separating camp from rusada
    for aircraft in request["request"]["aircraftDetails"]:
        if aircraft["maintenanceProvider"].upper() == "CAMP":
            logger.debug(request)
            camp_aircraft_details["aircraftDetails"].append(get_camp_aircraft_details(aircraft))

        if aircraft["maintenanceProvider"].upper() == "RUSADA":
            logger.debug(request)
            rusada_aircraft_details["aircraftDetails"].append(get_rusada_aircraft_details(aircraft))

    if camp_aircraft_details:
        camp_request = get_camp_request(camp_aircraft_details, request["request"]["supplierId"])
        return_code, return_type, camp_response = lambda_accessor.call_camp(camp_request)
        if len(camp_response["standardResponse"]["warnings"]) > 0:
            message.add_warnings(camp_response["standardResponse"]["warnings"])

    # if rusada_aircraft_details:
    #     rusada_request = get_rusada_request(rusada_aircraft_details, request["request"]["supplierId"])
    #     rusada_response = lambda_accessor.call_rusada(rusada_request)

    if return_code == 0 \
            and "aircraftList" in camp_response["responseMessage"] \
            and len(camp_response["responseMessage"]["aircraftList"]):
        response = camp_response["responseMessage"]["aircraftList"]
        return return_code, "Good", response
    else:
        return return_code, "FATAL", ""


def get_camp_aircraft_details(request):
    return {
        "maintenanceProvider": request["maintenanceProvider"],
        "secretName": request["secretName"],
        "keyPrefix": request["keyPrefix"],
        "modelName": request["modelName"],
        "regNo": request["regNo"],
        "serial": request["serial"]
    }


def get_camp_request(request, supplier_id):
    return {
        "context": {
            "domainName": "Order",
            "language": "EN",
            "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJKb2hubnkiLCJsYXN0TmFtZSI6IlJhYmJpdCIsImxvZ29uVHlwZSI6IlNBIiwic3VwcGxpZXJJZCI6NzAwMCwiYnVzaW5lc3NJZCI6MCwidXNlcklkIjozMzA2ODAxMCwiaXNzIjoiQ2hhcnRlciBhbmQgR28gYXV0aGVudGljYXRpb24iLCJleHAiOjE2MzE2MTk5MTh9.IfBL6Q6AdJzoiOg1oCfMg3u_dp67V8zmQ3F33Z_W4MN2YLirKeJ5gFHLN0kBhfFuQ9KhQ55AS2AOG6SMe4Ce4S2aNve9TAGWGFtXayYqX3hppnACreu-icG5PoqzPDZ6T0bc_hFuHoQgYuVIgGGo6hfx2HJ3ODgfMJR8237qds5SYpki-2hdlbJyddgfuRegN08HdGP3kfRm-b4xKMH_TKMpdxGVrLKQoslyI4uz8IpJGysHHUTtl5FUE4jaSUc1a3TsXudKt2jOzAh9vdw8Skll8rKEwNe46dRfZvCVuqwbHAwkYxa_o2Be3vr0y7glRpSvEBRI1eOxO0r2tqvWRQ"
        },
        "commonParms": {
            "action": "ReadAll",
            "view": "CAMP",
            "version": "1.0.0",
            "transactionId": "PETERG ORDER"
        },
        "request": {
            "supplierId": supplier_id,
            "aircraftDetails": request["aircraftDetails"]

        }
    }


def get_rusada_aircraft_details(request):
    return {
        "maintenanceProvider": request["maintenanceProvider"],
        "modelName": request["modelName"],
        "regNo": request["regNo"],
        "serial": request["serial"]
    }


def get_rusada_request(request, supplier_id):
    return {
        "context": {
            "domainName": "Order",
            "language": "EN",
            "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJKb2hubnkiLCJsYXN0TmFtZSI6IlJhYmJpdCIsImxvZ29uVHlwZSI6IlNBIiwic3VwcGxpZXJJZCI6NzAwMCwiYnVzaW5lc3NJZCI6MCwidXNlcklkIjozMzA2ODAxMCwiaXNzIjoiQ2hhcnRlciBhbmQgR28gYXV0aGVudGljYXRpb24iLCJleHAiOjE2MzE2MTk5MTh9.IfBL6Q6AdJzoiOg1oCfMg3u_dp67V8zmQ3F33Z_W4MN2YLirKeJ5gFHLN0kBhfFuQ9KhQ55AS2AOG6SMe4Ce4S2aNve9TAGWGFtXayYqX3hppnACreu-icG5PoqzPDZ6T0bc_hFuHoQgYuVIgGGo6hfx2HJ3ODgfMJR8237qds5SYpki-2hdlbJyddgfuRegN08HdGP3kfRm-b4xKMH_TKMpdxGVrLKQoslyI4uz8IpJGysHHUTtl5FUE4jaSUc1a3TsXudKt2jOzAh9vdw8Skll8rKEwNe46dRfZvCVuqwbHAwkYxa_o2Be3vr0y7glRpSvEBRI1eOxO0r2tqvWRQ"
        },
        "commonParms": {
            "action": "ReadAll",
            "view": "RUSADA",
            "version": "1.0.0",
            "transactionId": "PETERG ORDER"
        },
        "request": {
            "supplierId": supplier_id,
            "aircraftDetails": request["aircraftDetails"]
        }
    }
