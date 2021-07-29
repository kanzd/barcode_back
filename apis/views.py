from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status
from .models import UserModel


class LoginApiView(APIView):
    def post(self,req):

        user =UserModel.objects.filter(username=req.data["username"],password=req.data["password"])
        if len(user)==0:
            return Response({"message":"user not found","response_code":"0"})
        return Response({"message":"user found","response_code":"1","username":user[0].username})

class LoginValidateApiView(APIView):
    def post(self,req):

        user =UserModel.objects.filter(username=req.data["username"])
        if len(user)==0:
            return Response({"message":"user not found","response_code":"0"})
        return Response({"message":"user found","response_code":"1"})






