from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import *
from .serializers import *
import json

class UsersApiView(APIView):

    def get(self, request, *args, **kwargs):
        all_users = Users.objects.all().values()
        return Response({"status": "success", "data": all_users})

    def post(self, request, *args, **kwargs):
        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            given_bid_id = request.query_params.get('bid_id', None)

            if given_id is not None:
                filtered_bids = Bids.objects.filter(Q(party1_id=given_id) | Q(party2_id=given_id)).values()
                return Response({"status": "success", "data": filtered_bids})
            elif given_bid_id is not None:
                filtered_bids = Bids.objects.filter(Q(id=given_bid_id)).values()
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

    def put(self, request, *args, **kwargs):
        bid_id = kwargs.get('id', None)

        if bid_id is not None:
            try:
                bid_instance = Bids.objects.get(id=bid_id)
            except Bids.DoesNotExist:
                return Response({"status": "error", "message": "Bid not found"}, status=status.HTTP_404_NOT_FOUND)

            data = request.data.copy()
            other_parties_data = data.pop('other_parties', None)

            # Convert 'null' to an empty list
            existing_other_parties = bid_instance.other_parties
            existing_other_parties_list = json.loads(existing_other_parties) if existing_other_parties else []

            # Append the new data to the existing list or create a new list
            updated_other_parties = existing_other_parties_list + [data] if existing_other_parties_list else [data]

            # Update the bid instance with the new 'other_parties'
            bid_instance.other_parties = json.dumps(updated_other_parties)
            bid_instance.save()

            serializer = BidsSerializer(bid_instance)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "message": "Bid ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

class RefersApiView(APIView):

    def get(self, request, *args, **kwargs):
        all_refers = Refers.objects.all().values()
        return Response({"status": "success", "data": all_refers})

    def post(self, request, *args, **kwargs):
        serializer = RefersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        