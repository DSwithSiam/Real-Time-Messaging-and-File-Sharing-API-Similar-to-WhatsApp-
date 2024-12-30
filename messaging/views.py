from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework.permissions import isAuthenticated
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.models import User

from models import Message, Group
from serializers import GroupSerializer, MessageSerializer



class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(username = username, password = password)
        return Response({'message': 'User Registered Successfully.'}, status = 201)
