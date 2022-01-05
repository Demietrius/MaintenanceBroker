import json

from secret_manager import secret_manager
from unittest import TestCase

from broker import app


class Test(TestCase):

    def test_apigw_event(self):
        """ Generates API GW Event"""

        return {
            "body": {
                "context": {
                    "domainName": "Order",
                    "language": "EN",
                    "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJKb2hubnkiLCJsYXN0TmFtZSI6IlJhYmJpdCIsImxvZ29uVHlwZSI6IlNBIiwic3VwcGxpZXJJZCI6NzAwMCwiYnVzaW5lc3NJZCI6MCwidXNlcklkIjozMzA2ODAxMCwiaXNzIjoiQ2hhcnRlciBhbmQgR28gYXV0aGVudGljYXRpb24iLCJleHAiOjE2MzE2MTk5MTh9.IfBL6Q6AdJzoiOg1oCfMg3u_dp67V8zmQ3F33Z_W4MN2YLirKeJ5gFHLN0kBhfFuQ9KhQ55AS2AOG6SMe4Ce4S2aNve9TAGWGFtXayYqX3hppnACreu-icG5PoqzPDZ6T0bc_hFuHoQgYuVIgGGo6hfx2HJ3ODgfMJR8237qds5SYpki-2hdlbJyddgfuRegN08HdGP3kfRm-b4xKMH_TKMpdxGVrLKQoslyI4uz8IpJGysHHUTtl5FUE4jaSUc1a3TsXudKt2jOzAh9vdw8Skll8rKEwNe46dRfZvCVuqwbHAwkYxa_o2Be3vr0y7glRpSvEBRI1eOxO0r2tqvWRQ"
                },
                "commonParms": {
                    "action": "updateTotals",
                    "view": "CAMP",
                    "version": "1.0.0",
                    "transactionId": "PETERG ORDER"
                },
                "request": {
                    "aircraftDetails": {
                        "orderId": 123,
                        "orderItemId": 384,
                        "supplierId": 7000,
                        "maintenanceType": "Rusada",
                        "modelName": "CARAVAN 1 MODEL 208",
                        "regNo": "N-TXT20",
                        "serial": "208B-5360TEST2",
                        "flightType": 0,
                        "departurePlace": 0,
                        "arrivalPlace": 0,
                        "items": [
                            {
                                "profileType": "PROPELLER",
                                "serial": "160906TEST2",
                                "position": "NO. 1",
                                "unit": "HRS",
                                "lastReportedValue": "83226",
                                "startTime": "02-04-2021T10:00:00.4893",
                                "endTime": "02-04-2021T10:00:00.4893",
                                "lastReportedDate": "2021-04-27T00:00:00"
                            }
                        ]
                    }
                }
            },
            "resource": "/{proxy+}",
            "requestContext": {
                "resourceId": "123456",
                "apiId": "1234567890",
                "resourcePath": "/{proxy+}",
                "httpMethod": "POST",
                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
                "accountId": "123456789012",
                "identity": {
                    "apiKey": "",
                    "userArn": "",
                    "cognitoAuthenticationType": "",
                    "caller": "",
                    "userAgent": "Custom User Agent String",
                    "user": "",
                    "cognitoIdentityPoolId": "",
                    "cognitoIdentityId": "",
                    "cognitoAuthenticationProvider": "",
                    "sourceIp": "127.0.0.1",
                    "accountId": "",
                },
                "stage": "prod",
            },
            "queryStringParameters": {"foo": "bar"},
            "headers": {
                "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
                "Accept-Language": "en-US,en;q=0.8",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Mobile-Viewer": "false",
                "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
                "CloudFront-Viewer-Country": "US",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Upgrade-Insecure-Requests": "1",
                "X-Forwarded-Port": "443",
                "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
                "X-Forwarded-Proto": "https",
                "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
                "CloudFront-Is-Tablet-Viewer": "false",
                "Cache-Control": "max-age=0",
                "User-Agent": "Custom User Agent String",
                "CloudFront-Forwarded-Proto": "https",
                "Accept-Encoding": "gzip, deflate, sdch",
            },
            "pathParameters": {"proxy": "/examplepath"},
            "httpMethod": "POST",
            "stageVariables": {"baz": "qux"},
            "path": "/examplepath",
        }

    def test_lambda_handler1(self):
        print("insdie event")
        payload = {"context":{"domainName":"Maintenance","securityToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJQZXRlciIsImxhc3ROYW1lIjoiR29zc2VsbCIsImxvZ29uVHlwZSI6IkNBIiwic3VwcGxpZXJJZCI6MTAwMCwiYnVzaW5lc3NJZCI6MCwidXNlcklkIjozNzcxMTU4MCwiaXNzIjoiQ2hhcnRlciBhbmQgR28gYXV0aGVudGljYXRpb24iLCJleHAiOjE2NDE0MzkwOTR9.Bfb61sWJKsQro6WydhC3dB8ZIOW75xZmcK3c4lrFZHYozxoq_qAImG_TqnO-li02orfymaor4PzCWNXgc-NhR4CZbyRUqjMml0binRIkXsNcgX7snxCxMnCrZe7cmlu_x063ayruuCnYu-dBHI4sZyM_WURXWsdM-jQIv_YIHhuH9ESugUfJe525EJRp_-0SdI7lHyjBFtl4suF7BX9JjisZWy9U455A8TGWmQT45KItFMy3NE_lIAGfjHwMRRVTlehFH-1J2jpZrlmvgVwkL6C89Js5bwxzKDreCRLzZx0JqQA-UYGBsOV1Ly9RlCWtp3LbTYoj0qcesyKulG-PIp82AX6RUlhuuCptUdR92oafvbMbhi40Cupo3b4NttPxQiugZhhVBBqldNAq8SyIYTnK6rcEmSxslX8Noa4mk1V0iW4Bln0d8OxlHrZhRTTNI-p-np-BH6d8sUGdeKOC0R5QxXlmWJeG13nd8NbbCTtFyt-NQvQuQKiirrsbfQZS","language":"EN"},"commonParms":{"action":"GetValidAircraft","view":"CAMP","version":"1.0.0","transactionId":"PETERG ACCOUNTS"},"request":{"supplierId":7000,"maintenanceProvider":"CAMP","userName":"CGFLFEED0006c","account":"CAMP","status":"active","type":"maintenance","keyPrefix":"CGFLFEED0006c-CAMP","secretName":"7000-1-Profiles","lastUpdated":"2021-11-05 21:21:56.312993"}}
        response = app.lambda_handler(payload, " ")
        pass

    def test_lambda_handler(apigw_event, mocker):
        ret = app.lambda_handler(apigw_event, "")
        data = json.loads(ret["body"])

        assert ret["statusCode"] == 200
        assert "message" in ret["body"]
        assert data["message"] == "hello world"
        # assert "location" in data.dict_keys()

    def test_create_secret(self):
        session = boto3.session.Session()
        secretsmanager_client = session.client(
            service_name='secretsmanager',
            region_name="us-east-1"
        )
        name = "testCAMPName4"
        secret_value = json.dumps({"account": "CAMP",
                                   "username": "CGFLFEED0006",
                                   "password": "DB943WD6",
                                   "status": "active"})
        try:
            kwargs = {'Name': name}
            response = secretsmanager_client.create_secret(**kwargs)
            self.name = name
            print("Created secret %s.", name)
        except ClientError:
            print("Couldn't get secret %s.", name)
            raise
        else:
            print(response)
            return response

    def test_put_value(self, ):
        name = "7000-1-Profiles"
        session = boto3.session.Session()
        secretsmanager_client = session.client(
            service_name='secretsmanager',
            region_name="us-east-1"
        )
        secret = secret_manager.get_secrets(name)
        values = {}
        payload = {"account": "camp", "password": "DB943WD6", "status": "active"}
        values["CGFLFEED0006-Maintenance-CAMP-1"] = json.dumps(payload)
        new_secret = json.dumps(values)
        try:
            kwargs = {'SecretId': name}
            if isinstance(new_secret, str):
                kwargs['SecretString'] = new_secret
            elif isinstance(new_secret, bytes):
                kwargs['SecretBinary'] = new_secret
            response = secretsmanager_client.put_secret_value(**kwargs)
        except ClientError:
            raise
        else:
            return response

    def test_lambda_call(self):
        lambda_client = boto3.client("lambda", region_name="us-east-1")
        try:
            payload = {
                "context": {
                    "domainName": "Order",
                    "language": "EN",
                    "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJzdXBwbGllciIsImxhc3ROYW1lIjoiYWRtaW4iLCJsb2dvblR5cGUiOiJDQSIsInN1cHBsaWVySWQiOjEwMDAsImJ1c2luZXNzSWQiOjAsInVzZXJJZCI6NDQ5NjcxOTEsImlzcyI6IkNoYXJ0ZXIgYW5kIEdvIGF1dGhlbnRpY2F0aW9uIiwiZXhwIjoxNjMzNTY1MDQ4fQ.hfoYsZNmNYkSxE4n2HeK2UUg8mHu4QjUhnefoZM1H-WGZS5DquQuEjyB7zt4X_1e4fuXxtqn52z8Y8JLjK4IktAX808ed1WlG0uUTcdekRr1-WnBvpFoebU8vzrB-6r6TqU7hRAomANoszQXT61wWbAXWzE93bA9gNCSPpsD0NKkCHlGG6YoUTLqw7kfR4_GhEqLhKJ4nUTCksh17-seNs6_PrUQPT4OgUsJRlGfHaVMl4t-3zwJmy5HDMx4V2F6yXYaWpCr7JKj1OS4yWlAJZSqmkS0NS-13FHkGjHL82wtxdZbpYOk9Y3VmIoX19p7qXqezRNMi6bmqokn7a4J4w"
                },
                "commonParms": {
                    "action": "updateTotals",
                    "view": "CAMP",
                    "version": "1.0.0",
                    "transactionId": "PETERG ORDER"
                },
                "request": {
                    "supplierId": 7000,
                    "aircraftDetails": {
                        "orderId": 123,
                        "orderItemId": 384,
                        "supplierId": 7000,
                        "maintenanceType": "Rusada",
                        "modelName": "CARAVAN 1 MODEL 208",
                        "regNo": "N-TXT20",
                        "serial": "208B-5360TEST2",
                        "flightType": 0,
                        "departurePlace": 0,
                        "arrivalPlace": 0,
                        "items": [
                            {
                                "profileType": "PROPELLER",
                                "serial": "160906TEST2",
                                "position": "NO. 1",
                                "unit": "HRS",
                                "lastReportedValue": "83221",
                                "startTime": "02-04-2021T10:00:00.4893",
                                "endTime": "02-04-2021T10:00:00.4893",
                                "lastReportedDate": "2021-04-27T00:00:00"
                            }
                        ]
                    }
                }
            }

            response = lambda_client.invoke(
                FunctionName="MaintenanceBroker-Dev:Dev",
                InvocationType="RequestResponse",
                LogType='None',
                Payload=json.dumps(payload),
            )
            #  does response contain payload element
            if 'Payload' not in response:
                self.errorObj.add_error(19008, 'Invalid response from profiles', 'FATAL', 'Auto Close Handler')
                return 1, " ", " "
            if 'StatusCode' not in response or response['StatusCode'] != 200:
                self.errorObj.add_error(19009, 'Invalid response from profiles', 'FATAL', 'Auto Close Handler')
                return 1, " ", " "

            jsonString = response['Payload'].read()
            print(jsonString)
            pass
        except Exception as details:
            return 1, "FATAL", "Exception, retrieving supplier profiles"
