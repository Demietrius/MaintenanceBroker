import os
import Message
from ValidateToken import ValidateToken
from action_enum import action_enum
import maintenance_read
import maintenance_update
import maintenance_scheduler
import maintenance_logins
import cglogging as cgl

logger_Class = cgl.cglogging()
logger = logger_Class.setup_logging()


class RequestRouter:
    dashboard_ids = os.environ.get("CAG_DASHBOARD_IDS")

    @classmethod
    def router(cls, action, request):
        message = Message.Message()
        # these on environment variables that will be pulled on deployment
        logger.debug("inside router")

        if "securityToken" not in request["context"]:
            return message.get_fatal_standard_message(1)
        # return bad token if error
        errNum, return_type, errMsg = ValidateToken.validate_jwt(request["context"]["securityToken"])
        if errNum != 0:
            return message.get_response(errNum, "")

        if ValidateToken.get_swapSupplierId() != 0 and ValidateToken.get_authSupplierId() == 1000 \
                and ValidateToken.get_authLogonType() == "CA":
            parent_supplier = ValidateToken.get_swapSupplierId()
        elif ValidateToken.get_authSupplierId() == 1000 \
                and ValidateToken.get_authLogonType() == "ZA":
            parent_supplier = ValidateToken.get_swapSupplierId()
        else:
            parent_supplier = ValidateToken.get_authSupplierId()

        if ValidateToken.authBranchAccess is not None and len(ValidateToken.authBranchAccess) > 0:
            for branch in ValidateToken.authBranchAccess:
                if branch["account"] == "MASTER" and branch["supplierId"] != parent_supplier:
                    return message.get_fatal_standard_message(33001)
                if branch["account"] == "BRANCH" and branch["supplierId"] == request["request"]["supplierID"]:
                    supplier_id = branch["account"]

        else:
            supplier_id = parent_supplier

        # routing by actions
        if action.upper() == action_enum.Read.name.upper():
            logger.debug("getting aircraft and hours")
            if ValidateToken.get_authLogonType() not in ["SA", "SM", "SC", "CA", "SF", "SH", "ZA"]:
                return message.get_fatal_standard_message(33001)
            return_code, return_message, response = maintenance_read.handler_request(request)

        elif action.upper() == action_enum.updateTotals.name.upper():
            if ValidateToken.get_authLogonType() not in ["SA", "SM"] \
                    and (ValidateToken.get_authLogonType() != "ZA" and supplier_id != 1000) \
                    and (ValidateToken.get_authLogonType() != "CA" and supplier_id != 1000):
                return message.get_fatal_standard_message(33001)

            logger.debug("update hours")
            return_code, return_message, camp_message = maintenance_update.handler_request(request)
            response = camp_message["responseMessage"]
            for warning in camp_message["standardResponse"]["warnings"]:
                message.add_warnings(warning)
            logger.debug("done with updating totals")

        elif action.upper() == action_enum.GetMaintenance.name.upper():
            logger.debug("get maintenance")
            return_code, return_message, camp_message = maintenance_scheduler.handler_request(request)
            response = camp_message["responseMessage"]
            if camp_message["standardResponse"]["returnCode"] != 0:
                for warning in camp_message["standardResponse"]["warnings"]:
                    message.add_warnings(warning)
            elif return_code == 0:
                return camp_message

        elif action.upper() == action_enum.GetValidAircraft.name.upper():
            logger.debug("get getValidAircraft")
            return_code, return_message, camp_message = maintenance_logins.get_valid_aircraft_handler(request)
            if return_code == 33012:
                message.set_standard_response(camp_message["standardResponse"])
                return message.get_standard_response()

            elif camp_message["standardResponse"]["returnCode"] != 0:
                for warning in camp_message["standardResponse"]["warnings"]:
                    message.add_warnings(warning)
            elif return_code == 0:
                return camp_message

        elif action.upper() == action_enum.TestLogIn.name.upper():
            if ValidateToken.get_authLogonType() not in ["SA", "SM"] \
                    and (ValidateToken.get_authLogonType() != "CA" and supplier_id != 1000):
                return message.get_fatal_standard_message(33001)
            logger.debug("test Login")
            return_code, return_message, response = maintenance_logins.test_login_handler_request(request)
            if return_code == 33012:
                message.set_standard_response(response["standardResponse"])
                return message.get_standard_response()

        elif action.upper() == action_enum.SubmitLogin.name.upper():
            logger.debug("submit Login")
            return_code, return_message, response = maintenance_logins.submit_login_handler_request(request)

        elif action.upper() == action_enum.DeleteLogin.name.upper():
            logger.debug("delete Login")
            return_code, return_message, response = maintenance_logins.delete_login_handler(request)

        elif action.upper() == action_enum.GetAccounts.name.upper():
            logger.debug("delete Login")
            return_code, return_message, response = maintenance_logins.get_accounts(request)

        # return message logic
        if return_code == 0:
            return message.get_response(return_code, response)
        else:
            return message.get_fatal_standard_message(return_code)
