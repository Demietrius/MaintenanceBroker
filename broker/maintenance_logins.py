import json

import cglogging as cgl
from lambda_accessor import lambda_accessor
from secret_manager import secret_manager

logger_Class = cgl.cglogging()
logger = logger_Class.setup_logging()


def test_login_handler_request(request):
    if request["request"]["maintenanceProvider"].upper() == "RUSADA".upper():
        pass
    elif request["request"]["maintenanceProvider"].upper() == "CAMP".upper():
        return_code, return_type, response = lambda_accessor.call_camp(test_camp_login(request))
        if return_code == 0:
            return 0, "GOOD", response
        else:
            return return_code, "FATAL ", response


def submit_login_handler_request(request):
    if request["request"]["maintenanceProvider"].upper() == "RUSADA".upper():
        return submit_camp_login(test_rusada_login(request))

    elif request["request"]["maintenanceProvider"].upper() == "CAMP".upper():
        return submit_camp_login(request)


def delete_login_handler(request):
    if request["request"]["maintenanceProvider"].upper() == "RUSADA".upper():
        pass

    elif request["request"]["maintenanceProvider"].upper() == "CAMP".upper():
        return delete_camp_login(request)


def get_valid_aircraft_handler(request):
    if request["request"]["maintenanceProvider"].upper() == "RUSADA".upper():
        pass

    elif request["request"]["maintenanceProvider"].upper() == "CAMP".upper():
        return get_camp_login_aircrafts(request["request"]["secretName"],
                                        request["request"]["keyPrefix"],
                                        request["request"]["supplierId"])


def get_accounts(request):
    logger.debug("getting accounts")
    current_name = " "
    return_code = 0
    secret_names = []
    account = {"accounts": []}
    secret = " "
    previous_name = None
    index = 1
    while return_code == 0:
        current_name = str(request["request"]["supplierId"]) + "-" + str(index) + "-Profiles"
        return_code, return_type, secret = secret_manager.get_secrets(current_name)
        if return_code != 0 and index == 1:
            return return_code, return_type, " "
        elif return_code != 0 and index != 1:
            break
        previous_name = str(request["request"]["supplierId"]) + "-" + str(index) + "-Profiles"
        index += 1
        secret_names.append(current_name)

    for name in secret_names:
        return_code, return_type, secret = secret_manager.get_secrets(name)
        if return_code != 0:
            return return_code, " "

        extracted_secret = json.loads(secret["SecretString"])
        for key, value in extracted_secret.items():
            if len(value) < 1:
                continue
            temp_value = json.loads(value)
            deconstruct_account = {
                "userName": temp_value["userName"],
                "account": temp_value["account"],
                "status": temp_value["status"],
                "type": temp_value["type"],
                "keyPrefix": key,
                "secretName": name,
                "lastUpdated": temp_value["lastUpdated"]
            }
            account["accounts"].append(deconstruct_account)
    return 0, "Good", account


def get_credentials_handler(request):
    if request["request"]["maintenanceProvider"].upper() == "RUSADA".upper():
        pass

    elif request["request"]["maintenanceProvider"].upper() == "CAMP".upper():
        return get_camp_credentials(request)


def get_camp_credentials(request):
    current_name = " "
    return_code = 0
    previous_name = None
    index = 1
    while return_code == 0:
        current_name = str(request["request"]["supplierId"]) + "-" + str(index) + "-Profiles"
        return_code, return_type, secret = secret_manager.get_secrets(current_name)
        if return_code != 0 and index == 1:
            return return_code, return_type, " "
        elif return_code != 0 and index != 1:
            break
        previous_name = str(request["request"]["supplierId"]) + "-" + str(index) + "-Profiles"
        index += 1

    if previous_name:
        return_code, return_type, secret = secret_manager.get_secrets(previous_name)
    else:
        return_code, return_type, secret = secret_manager.get_secrets(current_name)

    extracted_secret = json.loads(secret["SecretString"])
    key = request["request"]["keyPrefix"]
    if key in extracted_secret:
        return 0, extracted_secret[key]
    else:
        return 33010, "Fatal", " "


def delete_camp_login(request):
    current_name = " "
    return_code = 0
    secret = " "
    previous_name = None
    index = 1
    while return_code == 0:
        current_name = str(request["request"]["supplierId"]) + "-" + str(index) + "-Profiles"
        return_code, return_type, secret = secret_manager.get_secrets(current_name)
        if return_code != 0 and index == 1:
            return return_code, return_type, " "
        elif return_code != 0 and index != 1:
            break
        previous_name = str(request["request"]["supplierId"]) + "-" + str(index) + "-Profiles"
        index += 1

    if previous_name:
        return_code, return_type, secret = secret_manager.get_secrets(previous_name)
    else:
        return_code, return_type, secret = secret_manager.get_secrets(current_name)

    extracted_secret = json.loads(secret["SecretString"])
    if request["request"]["keyPrefix"] in extracted_secret:
        del extracted_secret[request["request"]["keyPrefix"]]
        secret_manager.update_secret(secret["Name"], extracted_secret)
    else:
        return 33010, "Fatal", " "
    pass
    return 0, "GOOD", " "


def submit_camp_login(request):
    payload = {
        "context": {
            "domainName": "AccountPluginManager",
            "securityToken": request["context"]["securityToken"],
            "language": "EN"
        },
        "commonParms": {
            "action": "SubmitLogin",
            "view": "Account",
            "version": "1.0.0",
            "transactionId": "PETERG AIRCRAFT"
        },
        "request": {
            "supplierId": request["request"]["supplierId"],
            "account": {
                "account": request["request"]["maintenanceProvider"],
                "userName": request["request"]["userName"],
                "password": request["request"]["password"],
                "type": "maintenance"
            }
        }
    }

    return_code, return_type, response = lambda_accessor.call_account_plugin(payload)
    if return_code != 0:
        return return_code, return_type, " "
    if response["standardResponse"]["returnCode"] != 0:
        return return_code, return_type, response

    return_code, return_type, aircrafts = get_camp_login_aircrafts(response["responseMessage"]["secretName"],
                                                                   response["responseMessage"]["keyPrefix"],
                                                                   request["request"]["supplierId"])
    response["responseMessage"]["aircraftDetails"] = aircrafts["responseMessage"],


    return return_code, "GOOD", response


def get_camp_login_aircrafts(secretName, keyPrefix, supplierId):
    payload = {
        "context": {
            "domainName": "Order",
            "language": "EN",
            "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJzdXBwbGllciIsImxhc3ROYW1lIjoiYWRtaW4iLCJsb2dvblR5cGUiOiJDQSIsInN1cHBsaWVySWQiOjEwMDAsImJ1c2luZXNzSWQiOjAsInVzZXJJZCI6NDQ5NjcxOTEsImlzcyI6IkNoYXJ0ZXIgYW5kIEdvIGF1dGhlbnRpY2F0aW9uIiwiZXhwIjoxNjMzMzg3NTQ5fQ.QcHLdiG-s_WwD8t0_M_I5cf0WPaDP3VRe5pBydKbU0QnOs3-nePoUE35EqG8K8vMonc59C8T_7h4ndBzPWKOjZH0epIdoFHVG4baaK9Yn6sSYMhK3dbQUT61mWRwI5B_C2YNQYvdQnLJNzRPn6XproGWMKvtqm3JEyY69TIAMYRnLHGP5I8Mp8P7C2Kx9BKK2hSz2r2IemduA1ASvgArHArcC1St-t0ix_8z1zfgHCRkDve-qzz9RQwtnzcw2Km_gBTtfDbsFiS5yECypLknPu9E1VNZJHlXlekySCBOTnkdUkSxMl67-NXUiWE2UP_12T7TMB9ZL5e0pRXA1W2kuw"
        },
        "commonParms": {
            "action": "GetValidAircraft",
            "view": "CAMP",
            "version": "1.0.0",
            "transactionId": "PETERG ORDER"
        },
        "request": {
            "secretName": secretName,
            "keyPrefix": keyPrefix,
            "supplierId": supplierId

        }
    }
    return_code, return_type, response = lambda_accessor.call_camp(payload)
    return return_code, return_type, response


def test_rusada_login(request):
    return {
        "context": {
            "domainName": "Maintenance",
            "language": "EN",
            "securityToken": request["context"]["securityToken"]
        },
        "commonParms": {
            "action": "testLogin",
            "view": "RUSADA",
            "version": "1.0.0",
            "transactionId": "PETERG ORDER"
        },
        "request": {
            "supplierId": request["request"]["supplierId"],
            "maintenanceProvider": "RUSADA",
            "userName": request["request"]["userName"],
            "password": request["request"]["password"]
        }
    }


def test_camp_login(request):
    return {
        "context": {
            "domainName": "Maintenance",
            "language": "EN",
            "securityToken": request["context"]["securityToken"]
        },
        "commonParms": {
            "action": "testLogin",
            "view": "CAMP",
            "version": "1.0.0",
            "transactionId": "PETERG ORDER"
        },
        "request": {
            "supplierId": request["request"]["supplierId"],
            "maintenanceProvider": "CAMP",
            "userName": request["request"]["userName"],
            "password": request["request"]["password"]
        }
    }
