import json
import datetime


class Message:

    def __init__(self):
        self.dictionary = {0: " ",
                           1:" ",
                           33001: "Bad token",
                           33002: "Secret Manager Failed",
                           33003: "Validate Token Error",
                           33004: "Token corrupted",
                           33005: "Camp failed on lambda call",
                           33006: "Rusada failed on lambda call",
                           33007: "Invalid JSON in payload from camp ",
                           33008: "Invalid JSON in payload from Rusada",
                           33009: "Exception, unexpected error Auto Close Handler",
                           33010: "missing KeyPrefix from message",
                           33011: "Missing StandardResponse From Proxy",
                           33012: "Bad return code From Proxy."

                           }
        self.message = {"standardResponse": {}, "responseMessage": {}}
        self.warnings = {"warnings": []}

    def add_warnings(self, warning):
        self.warnings["warnings"].append(warning)

    def get_response(self, err_num, response):

        if err_num == 0:
            self.message["standardResponse"] = self.get_good_standard_message()["standardResponse"]
            self.message["responseMessage"] = response
            print(json.dumps(self.message))
            return self.message

        else:
            self.message["standardResponse"] = self.get_fatal_standard_message(err_num)["standardResponse"]
            self.message["responseMessage"] = response
            print(json.dumps(self.message))
            return self.message

    def set_standard_response(self, standard_response):
        self.message["standardResponse"] = standard_response

    def get_standard_response(self):
        return self.message

    def get_good_standard_message(self):
        return {
            "standardResponse": {
                "count": 0,
                "domain": "CAMP",
                "errorMessage": "",
                "language": "EN",
                "responseType": "GOOD",
                "returnCode": 0,
                "timeStampOfMessage": format(datetime.datetime.utcnow()),
                "warnings": self.warnings["warnings"]
            }
        }

    def get_fatal_standard_message(self, err_num):
        return {
            "standardResponse": {
                "count": 0,
                "domain": "CAMP",
                "errorMessage": self.dictionary[err_num],
                "language": "EN",
                "responseType": "FATAL",
                "returnCode": err_num,
                "timeStampOfMessage": format(datetime.datetime.utcnow()),
                "warnings": self.warnings["warnings"]
            }
        }
