from django.shortcuts import render
from rest_framework import status , viewsets
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import File
from rest.app.fileUpDown.serializers import FileSerializer
from django.http import HttpResponse
# Create your views here.


class UploadView(APIView):
    serializer_class=FileSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        custom_data={}
        custom_data['file']=request.data['file']
        custom_data['userid']=request.user.id
        print(custom_data['userid'])
        file_serializer = self.serializer_class(data=custom_data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
