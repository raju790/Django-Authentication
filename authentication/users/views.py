from django.shortcuts import render
from rest_framework.views import APIView
from .seralizers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


# view for creating users
class Users_SignUp(APIView):
    def post(self, request):
        email = request.data['email']
        request.data['username'] = email
        password = request.data['password']
        if None in [email, password]:
                        return Response({'error_message': "Please provide required details"}, status=status.HTTP_400_BAD_REQUEST)
        if password != request.data['confirmPassword']:
            return Response({'error_message': "confirmPassword doesn't match with password"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)