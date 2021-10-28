from lambda_accessor import lambda_accessor


def handler_request(request):
    if request["commonParms"]["view"].upper() == "RUSADA".upper():
        pass

    elif request["commonParms"]["view"].upper() == "CAMP".upper():
        return get_camp_maintenace(request)


def get_camp_maintenace(request):
    payload = {
        "context": {
            "domainName": "Maintenance",
            "language": "EN",
            "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJzdXBwbGllciIsImxhc3ROYW1lIjoiYWRtaW4iLCJsb2dvblR5cGUiOiJDQSIsInN1cHBsaWVySWQiOjEwMDAsImJ1c2luZXNzSWQiOjAsInVzZXJJZCI6NDQ5NjcxOTEsImlzcyI6IkNoYXJ0ZXIgYW5kIEdvIGF1dGhlbnRpY2F0aW9uIiwiZXhwIjoxNjMzNTIwNzk5fQ.WGrZ2yRL3bG9X2NA49jEV8LOOqU2hDq2n1SFXH7JG2KVTb8tX5Ov1srdSyICPTSWAUAKvX8si8r66_XfBI03j8XKZ9gRwNfbgK3qd2dgl_q4tj2vARwagoF9l04KoTSK7D5YmXVFnLKgChA3bZTO8DGrnNcM1ungqd4jFOqYJPKhbTY1LbgOh-YwpGFMZojCgU3VmS2wCg0JDDH2PIkcICyHi0VC6YmTs3Iq9HW35temucLCwQVMJTsE6yshJLCI24pGywWxAhetoC21-s9s0-MajCTjIXJt_XvAV5SzC2KFsqI2LfFxyYi9flNJVw2ZxlRsZrYPmAXV82wVe_stng"
        },
        "commonParms": {
            "action": "GetDueList",
            "view": "CAMP",
            "version": "1.0.0",
            "transactionId": "PETERG ORDER"
        },
        "request": {
            "supplierId": request["request"]["supplierId"],
            "aircraftDetails": {
                "secretName": request["request"]["aircraftDetails"]["secretName"],
                "keyPrefix": request["request"]["aircraftDetails"]["keyPrefix"],
                "modelName": request["request"]["aircraftDetails"]["modelName"],
                "regNo": request["request"]["aircraftDetails"]["regNo"],
                "serial": request["request"]["aircraftDetails"]["serial"],
                "dateRange": request["request"]["aircraftDetails"]["dateRange"],
            }
        }
    }

    return lambda_accessor.call_camp(payload)
