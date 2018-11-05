from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from blog.serializers import SayHello


@api_view(http_method_names=['POST', 'GET'])
def say_hello(request: Request):
    serializer = SayHello(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    if data.get('name'):
        mess = "hello {}".format(data.get('name'))

    return Response({
        'mess': mess
    })

