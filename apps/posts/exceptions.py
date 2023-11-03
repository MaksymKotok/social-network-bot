from rest_framework.exceptions import APIException


class PostNotFoundException(APIException):
    status_code = 400
    default_detail = "Post not found with given id!"
    default_code = "post_not_found"
