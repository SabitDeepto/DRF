# from rest_framework import serializers
from django.shortcuts import render
# from rest_framework_simplejwt import serializers
#
# from rest_project.serializers import TokenObtainPairPatchedSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
#
#
# class TokenObtainPairPatchedView(TokenObtainPairView):
#     """
#     Takes a set of user credentials and returns an access and refresh JSON web
#     token pair to prove the authentication of those credentials.
#     """
#     serializer_class = serializers.TokenObtainPairPatchedSerializer
#
#     token_obtain_pair = TokenObtainPairView.as_view()


def admin_view(request):
    return render(request, 'auth_login.html')