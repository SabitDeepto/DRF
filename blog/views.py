from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from blog.serializers import SayHelloSerializer


@api_view(http_method_names=['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def say_hello(request: Request):
    message = "hello"
    # if request.POST.get('name'):
    #     message = "Hello, " + request.POST.get('name')
    # if request.POST.get('dob'):
    #     try:
    #         dob = datetime.strptime(request.POST.get('dob'), '%Y-%m-%d')
    #     except ValueError as e:
    #         raise ValidationError(str(e))
    #     age = (datetime.now()-dob).days/365
    #     if age >= 30:
    #         message += " Sir !"
    # return Response({
    #     'message': message,
    # })

    serializer = SayHelloSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    if data.get('name'):
        message = "hello" + data.get('name')

        if data.get('dob'):
            age = (datetime.today().date()-data.get('dob')).days/365

            if age > 30:
                message += 'Sir'

    return Response({
        'message': message
    })

