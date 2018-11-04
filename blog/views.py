from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(http_method_names=['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def say_hello(request: Request):
    message = "hello"
    if request.POST.get('name'):
        message = "Hello, " + request.POST.get('name')
    if request.POST.get('dob'):
        try:
            dob = datetime.strptime(request.POST.get('dob'), '%Y-%m-%d')
        except ValueError as e:
            raise ValidationError(str(e))
        age = (datetime.now()-dob).days/365
        if age >= 30:
            message += " Sir !"
    return Response({
        'message': message,
    })


