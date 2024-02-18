from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
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
            return Response({"status": "success", "message": "Login successful", "user_type": user.user_type, "name": user.name, "username": user.username, "email": user.email, "phone": user.phone ,"id": user.id})
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def patch(self, request, *args, **kwargs):
        user_id = request.data.get('id', None)
        if not user_id:
            return Response({"error": "User ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsersSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        
class ItemsCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ItemsCategory.objects.all()
    serializer_class = ItemsCategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {'status': 'success', 'data': serializer.data}
        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'status': 'success', 'data': serializer.data}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class ItemsSubCategoriesListCreateView(generics.ListCreateAPIView):
    queryset = ItemsSubCategories.objects.all()
    serializer_class = ItemsSubCategoriesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {'status': 'success', 'data': serializer.data}
        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'status': 'success', 'data': serializer.data}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class ItemsSubCategoriesByCategoryView(generics.ListAPIView):
    serializer_class = ItemsSubCategoriesSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = ItemsSubCategories.objects.filter(category_id=category_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {'status': 'success', 'data': serializer.data}
        return Response(data)
  
class DashboardDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Count users
        total_users = Users.objects.count()

        # Count bids
        total_bids = Bids.objects.count()

        # Count refers
        total_refers = Refers.objects.count()

        # Count live one-time bids
        one_time_bids = Bids.objects.filter(bid_type='one_time').count()

        # Count live real-time bids
        real_time_bids = Bids.objects.filter(bid_type='real_time').count()

        # Count on going bids
        on_going_bids = Bids.objects.filter(bid_status='one_time').count()

        # Count on finished bids
        finished_bids = Bids.objects.filter(bid_status='finished').count()
        
        # Count users by type (supplier, manufacturer)
        users_by_type = {
            'supplier': Users.objects.filter(user_type='supplier').count(),
            'manufacturer': Users.objects.filter(user_type='manufacturer').count(),
        }

        data = {
            'total_users': total_users,
            'total_bids': total_bids,
            'total_refers': total_refers,
            'one_time_bids': one_time_bids,
            'real_time_bids': real_time_bids,
            'on_going_bids': on_going_bids,
            'finished_bids': finished_bids,
            'users_by_type': users_by_type,
        }

        return Response(data)


@api_view(['GET'])
def get_approval_status(request, bid_id):
    try:
        bid = Bids.objects.get(id=bid_id)
        serializer = BidsSerializer(bid)
        return Response({'status': serializer.data['is_approved'] == 'yes'})
    except Bids.DoesNotExist:
        return Response({'status': False, 'error': 'Bid not found'}, status=status.HTTP_404_NOT_FOUND)
    