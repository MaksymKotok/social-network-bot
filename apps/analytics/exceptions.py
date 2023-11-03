from rest_framework.exceptions import APIException


class IncorrectDateRangeException(APIException):
    status_code = 400
    default_detail = "Incorrect date range!"
    default_code = "incorrect_date_range"
