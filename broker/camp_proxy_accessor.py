import os

from lambda_accessor import lambda_accessor


def get_schedule(request):
    return_code, return_type, response = lambda_accessor.call_lambda(os.getenv("CAG_CAMP_FUNCTION"), request)
    return return_code, return_type, response

def update_hours(request):
    return_code, return_type, response = lambda_accessor.call_lambda(os.getenv("CAG_CAMP_FUNCTION"), request)
    return return_code, return_type, response