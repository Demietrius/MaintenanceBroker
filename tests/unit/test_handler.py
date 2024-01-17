import json

import boto3
from botocore.exceptions import ClientError

from secret_manager import secret_manager
from unittest import TestCase

from broker import app


class Test(TestCase):

    def test_apigw_event(self):
        """ Generates API GW Event"""

        return {
            "context": {
                "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJTeXN0ZW0iLCJsYXN0TmFtZSI6IkRvbWFpblRvRG9tYWluIiwibG9nb25UeXBlIjoiWkEiLCJzdXBwbGllcklkIjoxMDAwLCJidXNpbmVzc0lkIjowLCJ1c2VySWQiOjM5NDMwODY1LCJpc3MiOiJDaGFydGVyIGFuZCBHbyBhdXRoZW50aWNhdGlvbiIsImV4cCI6MTY3MjgwMjA1Nn0.JfBUCc09sTFVTKgBPN-VfVoC2Ya2pSVG86DOuV-3kYaY5lMicHLF9fYBLi9CB6f33i0FAt5cjtaOgstl-iAdoaFFGUyi36sTwREv_oM2rUXIgYpWz0LzVucFNam0C5OwkGzK2EOvWZdB4mEAP62ytdssCBxzE8FIY0WsybSUthwp28UZeb8TfmsUMLNx16famru15nkhihA8kUZ52kBifQoNNe0Pm1FA15UCt7Cx7OMuNGtelF1BTRL8O9ga8STLxe5xvlbdp_we_mZEE_sCnbQzzjiSnLCpqL4d9PUYnDG7Gp3aYThhkNAVbhx_Dhd_62AzEPyGpyPEpNnZBZnaeRQVRD0Z1ru5SheStRAyEhSf2tJ2quOQnheS0Gf1uFO2d8F7S3_xKVO4A-lBbnLhN5JRZxH1Xlr6h1WORXUVETN4gGm1iTpdQeurprrH5BIANC2FMeOBgJyWH0NzWlRbHvJ-v3NVxAFxPmLn3Hflbddclv8u-2bwvaGCAeWXYMLV",
                "transactionid": "AircraftToCampHandler123",
                "domainName": "MaintBroker",
                "language": "EN"
            },
            "commonParms": {
                "action": "updateTotals",
                "view": "Maintenance",
                "version": "1.0.0",
                "client": "AircraftToCampHandler"
            },
            "request": {
                "supplierId": 7000,
                "aircraftDetails": [
                    {
                        "secretName": "7000-1-Profiles",
                        "keyPrefix": "CGFLFEED0006-CAMP",
                        "orderId": 0,
                        "orderItemId": 0,
                        "maintenanceProvider": "CAMP",
                        "modelName": "G200",
                        "regNo": "N-TXT3",
                        "serial": "680A-0258TEST",
                        "flightType": 0,
                        "departurePlace": "",
                        "arrivalPlace": "",
                        "items": [
                            {
                                "profileType": "ENGINE",
                                "serial": "PCE-CN0524TEST",
                                "position": 2,
                                "unit": "HRS",
                                "lastReportedValue": 3800,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887698+00:00"
                            },
                            {
                                "profileType": "ENGINE",
                                "serial": "PCE-CN0524TEST",
                                "position": 2,
                                "unit": "ENC",
                                "lastReportedValue": 59,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887721+00:00"
                            },
                            {
                                "profileType": "ENGINE",
                                "serial": "PCE-CN0523TEST",
                                "position": 1,
                                "unit": "ENC",
                                "lastReportedValue": 58,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887736+00:00"
                            },
                            {
                                "profileType": "ENGINE",
                                "serial": "PCE-CN0523TEST",
                                "position": 1,
                                "unit": "HRS",
                                "lastReportedValue": 3810,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887751+00:00"
                            },
                            {
                                "profileType": "AIRCRAFT",
                                "serial": "680A-0258TEST",
                                "position": 0,
                                "unit": "ON-IN",
                                "lastReportedValue": 36,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887766+00:00"
                            },
                            {
                                "profileType": "AIRCRAFT",
                                "serial": "680A-0258TEST",
                                "position": 0,
                                "unit": "OUT-OFF",
                                "lastReportedValue": 50,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887781+00:00"
                            },
                            {
                                "profileType": "PROPELLER",
                                "serial": "1234-TEST",
                                "position": 0,
                                "unit": "HRS",
                                "lastReportedValue": 240,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887797+00:00"
                            },
                            {
                                "profileType": "APU",
                                "serial": "P-975TEST",
                                "position": 0,
                                "unit": "APUS",
                                "lastReportedValue": 122,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887812+00:00"
                            },
                            {
                                "profileType": "APU",
                                "serial": "P-975TEST",
                                "position": 0,
                                "unit": "HRS",
                                "lastReportedValue": 1930,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887827+00:00"
                            },
                            {
                                "profileType": "AIRCRAFT",
                                "serial": "680A-0258TEST",
                                "position": 0,
                                "unit": "AFL",
                                "lastReportedValue": 2474,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887841+00:00"
                            },
                            {
                                "profileType": "AIRCRAFT",
                                "serial": "680A-0258TEST",
                                "position": 0,
                                "unit": "HRS",
                                "lastReportedValue": 84486,
                                "startTime": "",
                                "endTime": "",
                                "lastReportedDate": "2022-06-24 21:03:43.887855+00:00"
                            }
                        ]
                    }
                ]
            }
        }

    def test_debug(self):
        payload = {"context": {
            "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJEZW1pZXRyaXVzIiwibGFzdE5hbWUiOiJIdWZmIiwibG9nb25UeXBlIjoiQ0EiLCJzdXBwbGllcklkIjoxMDAwLCJidXNpbmVzc0lkIjowLCJ1c2VySWQiOjI2MjIyNjg1LCJpc3MiOiJDaGFydGVyIGFuZCBHbyBhdXRoZW50aWNhdGlvbiIsImV4cCI6MTY2Njg0MjcwM30.ZSkb7k6qDWpzKOe83cm4qboYbIBumKgV4l-IU0Mrnw5NPuuSSfMkpcemuGR7auWTcQwMPhTo9rcwLj0323hJyhZl3hx7z90hAGBA8TTngHvWU9nwMIpSpAlckYOQ9ep443B_Y2jZNqNBrPppHME6h3H21p3cBXdnAu1J8EKN2vmwUgPRqUMoNxBK2y1Ml3zQZmcKaEThDgWOxKJHLOcgzd_wgIVCJlxe57E3bWjBho-tiPZ2ZmqYLpCyl-vGmGI-KTdwm1NVQ7jgEQsleS0CHqNSfN91TNm8D-ijz4ct0xSNMbbtXoHD2iHRevc2oF5_6AMk0tFTE2Ofy82V97WtuObhLIRtRvLpwnpO3zOBzGCtmdS-FUDuMy5HPtDxPQVmdGe6_4qENOTdJakKzJAIe_lBYrx4tdklmE53QEU7z4ZTlYB88L3SLV1i-dYu2Lk0bsOG2bPfjGMwtY4NjeD2qqfeSBuI3dN_j7y3Vxte1r6_S1c2nm4iO1lkni8Utch1",
                      "domainName": "Maintenance", "language": "EN", "client": "CAG POS",
            "transactionId": "753b4026-227b-4a65-acb5-ddc8bffcf6b6"},
                   "commonParms": {"action": "GetValidAircraft", "view": "CAMP", "version": "1.0.0"},
                   "request": {"supplierId": 7000, "maintenanceProvider": "CAMP", "userName": "CGFLFEED0006",
                               "account": "CAMP", "status": "active", "type": "maintenance",
                               "keyPrefix": "CGFLFEED0006-CAMP", "secretName": "7000-1-Profiles",
                               "lastUpdated": "2022-01-06 21:26:15.939561"}}
        response = app.lambda_handler(payload, " ")

    def test_lambda_handler1(self):
        print("insdie event")
        payload = {'context': {
            'securityToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJzdXBwbGllciIsImxhc3ROYW1lIjoiYWRtaW4iLCJsb2dvblR5cGUiOiJDQSIsInN1cHBsaWVySWQiOjEwMDAsImJ1c2luZXNzSWQiOjAsInVzZXJJZCI6NDQ5NjcxOTEsImlzcyI6IkNoYXJ0ZXIgYW5kIEdvIGF1dGhlbnRpY2F0aW9uIiwiZXhwIjoxNjU3NTgxNjA4fQ.fzQc3q0hbFW-lJeFB0yR22E68hzOYVal5cwE87bbzdLH-1iSBhmFQUG47LBG9OYEIBrdncdSAJpbyoUt6DOhrFAxZs6pOXf1lfozSyCybcfPg3PeEl6-SS4WJ_Xp8l5SkeOzF0cdgcjAIcioGeO8dQzeXlwlMmF7WUbvjNz1c04s8ZjhIbVxRJ7gJTfXbs-3e2eKcKZY8VwRhF6yw-Gcwj0lKpJSEPFTbhcjj5Z19d79sWld0GgBp_PmY26akAf7p209wJhdVrOpFS7dLXpIPUY2B-3i1C7PfIJ7BNMfulFQKXUruephWMzWanOO9_VEtQxCfKWg9W2zwAxe0Jy-ODLF5JA5rDD-4n86LnAzxVdgs2lGZxb5yrUyvo2mFYZtxcCDx769ueIrhAKgecgyeY9yk3lIzdnO7s4mq9wCuq8Alehc38-mX2QXeSxerUvDKFkzRD6JzaVbprvUhStM4lGUu7NBxrHKVUCn51P3pne6yPZbQ9p_B14uqlzaIH5v',
            'domainName': 'Maintenance', 'language': 'EN', 'client': 'CAG POS',
            'transactionId': '99007ac4-f464-4ab1-b083-b540a926cb36'},
                   'commonParms': {'action': 'GetMaintenance', 'view': 'DEFAULT', 'version': '1.0.0'},
                   'request': {'supplierId': 7000,
                               'aircraftDetails': {'maintenanceProvider': '', 'modelName': 'G200', 'regNo': 'N-TXT8',
                                                   'serial': '680A-0258TEST', 'dateRange': 120}}}

        response = app.lambda_handler(payload, " ")
        pass

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

    def test_getValidAircraft(self):
        payload = {
            "context": {
                "domainName": "Maintenance",
                "securityToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmaXJzdE5hbWUiOiJQZXRlciIsImxhc3ROYW1lIjoiR29zc2VsbCIsImxvZ29uVHlwZSI6IkNBIiwic3VwcGxpZXJJZCI6MTAwMCwiYnVzaW5lc3NJZCI6MCwidXNlcklkIjozNzcxMTU4MCwiaXNzIjoiQ2hhcnRlciBhbmQgR28gYXV0aGVudGljYXRpb24iLCJleHAiOjE2NDYzNTIyMDN9.I2IaZ2MWWf8dftIjrhQjrNmegMHyRwmZPQXplIs8XX0fTyKvx7ETEf7WCjjMMec9CsiUe6PPpzTAqa4B6DhTmaD6r0dfCgvfWbK0WaljyGoDfHlG8W9nW4AwC94Myu9NQdYEvzb3bt7JfktYu80WNn6sysEDzuWwJ3iUftI46aWazUYPCONRClVajllKQ3TEEA3ZrwVoH0qJ4VnnbD0Xi_mIP8AHFEzTp1aHFZLg7m9geryHSKquASDcEHf9TiHNMROWtW2HtE4pLg9NfTFMymcD1XRUU9vLOK_HDlmgy_RVTcyL4gbHiW3KDfn-UuWLYghAtnQgqLtNz8i3chGpE6dAAu3jGOKhKXJkko0RIMLl7H-pK3vTJ3mvE-2wceMaHyvnR-jzSYaJhHmflHm790YcEiMbCK5G2Bg-s8FV92dIW-xTsCcvJLCljnvcjRdJajW1tu3cecQ8flq0DyeXEgifS-SowTxLqcA-wYjInozKs-4JDhh2r0nf8tKL1MbG",
                "language": "EN"
            },
            "commonParms": {
                "action": "GetValidAircraft",
                "view": "CAMP",
                "version": "1.0.0",
                "transactionId": "PETERG ACCOUNTS"
            },
            "request": {
                "supplierId": 7000,
                "maintenanceProvider": "CAMP",
                "userName": "CGFLFEED0006",
                "account": "CAMP",
                "status": "active",
                "type": "maintenance",
                "keyPrefix": "CGFLFEED0006-CAMP",
                "secretName": "7000-1-Profiles",
                "lastUpdated": "2022-01-06 21:26:15.939561"
            }
        }
        ret = app.lambda_handler(payload, " ")
