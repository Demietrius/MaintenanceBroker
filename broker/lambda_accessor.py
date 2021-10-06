import json
import os

import boto3
import cglogging as cgl

logger_Class = cgl.cglogging()
logger = logger_Class.setup_logging()


class lambda_accessor:
    lambda_client = boto3.client("lambda", region_name=os.environ.get("CAG_REGION"))
    functionName = " "

    @classmethod
    def call_camp(self, request):
        self.functionName = os.getenv("CAG_CAMP_FUNCTION")
        return_code, return_type, response = self.call_lambda(request)
        logger.debug("done with camp")
        return return_code, return_type, response

    @classmethod
    def call_rusada(self, request):
        self.functionName = os.getenv("CAG_RUSADA_FUNCTION")
        return_code, return_type, response = self.call_lambda(request)
        return return_code, return_type, response

    @classmethod
    def call_lambda(self, payload):
        try:
            response = self.lambda_client.invoke(
                FunctionName=self.functionName,
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

            #  validate json response
            if len(jsonString) <= 0:
                return 1, "FATAL", "Invalid JSON in payload from business profiles"

            responseObj = json.loads(jsonString)
            logger.debug("JSON String Response from profile: {}".format(responseObj))
            # add message validation on the response and take error

            if 'standardResponse' not in responseObj:
                return 1, "FATAL", "No standard response element in response from profiles"

            if responseObj['standardResponse']['returnCode'] != 0:
                return 1, "FATAL", "Invalid return code from business profiles"

            return 0, "GOOD", responseObj

        except Exception as details:
            logger.error('Unexpected error: {0}'.format(details))
            return 1, "FATAL", "Exception, retrieving supplier profiles"
