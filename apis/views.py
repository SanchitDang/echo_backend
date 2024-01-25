from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import *
from .serializers import *

class UsersApiView(APIView):

    def get(self, request, *args, **kwargs):
        all_users = Users.objects.all().values()
        return Response({"status": "success", "data": all_users})

    def post(self, request, *args, **kwargs):
        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            serialized_user = UsersSerializer(user).data  # Include the id field in the response
            return Response(serialized_user, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            user = None

        if user is not None and user.password == password:
            return Response({"status": "success", "message": "Login successful", "user_type": user.user_type, "name": user.name, "id": user.id})
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UsersByTypeApiView(APIView):

    def get(self, request, *args, **kwargs):
        user_type = request.query_params.get('user_type', None)
        if user_type is not None:
            users = Users.objects.filter(user_type=user_type)
            serializer = UsersSerializer(users, many=True)
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"error": "user_type parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

class BidsApiView(APIView):

    def get(self, request, *args, **kwargs):
            given_id = request.query_params.get('id', None)

            if given_id is not None:
                filtered_bids = Bids.objects.filter(Q(party1_id=given_id) | Q(party2_id=given_id)).values()
                return Response({"status": "success", "data": filtered_bids})
            else:
                all_bids = Bids.objects.all().values()
                return Response({"status": "success", "data": all_bids})
    
    def post(self, request, *args, **kwargs):
            serializer = BidsSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
