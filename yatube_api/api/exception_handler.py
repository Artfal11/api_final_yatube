from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.views import exception_handler


def custom_jwt_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, InvalidToken):
        response.data = {
            'detail': 'Token is invalid or expired',
            'code': 'token_not_valid'
        }

    return response
