ERROR_MESSAGE = {
    50001: 'INVALID PARAM',
    50002: 'DATABASE CONNECT ERROR',
    50003: 'NO RESULT',
    50004: 'ERROR PARAM FORMAT',
}


def error_response(status, message='UNEXPECTED ERROR'):
    res = {
        'status': status,
        'message': ERROR_MESSAGE.get(status, message)
    }
    return res
