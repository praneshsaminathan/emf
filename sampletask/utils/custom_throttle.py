import logging
from rest_framework import response
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

LOGGER = logging.getLogger('api')


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, Throttled):
        # import pdb; pdb.set_trace()
        custom_response_data = {
            'message': 'request limit exceeded',
            'availableIn': '%d seconds'%exc.wait,
            'pranesh': "ldfjglkj"
        }
        # try:
        #     client_address = contextrequest.META[‘HTTP_X_FORWARDED_FOR’]
        # except:
        #     client_address = request.META[‘REMOTE_ADDR’]
        # LOGGER.error({})
        response.data = custom_response_data # set the custom response data on response object

    return response