from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import json
from .models import *
from .serializers import *
from home.models import Assessments,Banner
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
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
            return Response({"status": "success", "message": "Login successful", "user_type": user.user_type, "name": user.name, "username": user.username, "email": user.email, "phone": user.phone, "is_approved":user.is_approved, "id": user.id})
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


@method_decorator(csrf_exempt, name='dispatch')
class ScrapsApiVIew(APIView):
    
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            scraps = Scraps.objects.filter(user_id=user_id)
            serializer = ScrapsSerializer(scraps, many=True)
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "message": "user_id parameter is required"})
        
    def post(self, request, *args, **kwargs):
        serializer = ScrapsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    


@method_decorator(csrf_exempt, name='dispatch')
class ServicessApiVIew(APIView):
    
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            services = Services.objects.filter(user_id=user_id)
            serializer = ServicesSerializer(services, many=True)
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "message": "user_id parameter is required"})
        
    def post(self, request, *args, **kwargs):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    


@method_decorator(csrf_exempt, name='dispatch')
class UsersByTypeApiView(APIView):

    def get(self, request, *args, **kwargs):
        user_type = request.query_params.get('user_type', None)
        if user_type is not None:
            users = Users.objects.filter(user_type=user_type)
            serializer = UsersSerializer(users, many=True)
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"error": "user_type parameter is required"}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
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


@method_decorator(csrf_exempt, name='dispatch')
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


@method_decorator(csrf_exempt, name='dispatch')        
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


@method_decorator(csrf_exempt, name='dispatch')
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
    

@method_decorator(csrf_exempt, name='dispatch')
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


@method_decorator(csrf_exempt, name='dispatch')  
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


@method_decorator(csrf_exempt, name='dispatch')
class AssessmentApiView(APIView):

    def get(self, request, *args, **kwargs):
        assessment_id = request.data.get('id', None)
        if assessment_id is None:
            return Response({"error": "Assessment ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        assessments = Assessments.objects.get(id=assessment_id)
        return Response({"status": "success", "data": assessments})


    def post(self, request, *args, **kwargs):
        serializer = AssessmentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs):
        assessment_id = request.data.get('id', None)
        if not assessment_id:
            return Response({"error": "Assessment ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            assessment = Assessments.objects.get(id=assessment_id)
        except Assessments.DoesNotExist:
            return Response({"error": "Assessment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AssessmentsSerializer(instance=assessment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def get_products(request,user_id):
    if user_id == 'all':
        products = Products.objects.all().values()
        return Response({"status": "success", "data": products})
    products = Products.objects.filter(user_id=user_id)
    serializer = ProductsSerializer(products, many=True)
    return Response({"status": "success", "data": serializer.data})


@api_view(['POST'])
@csrf_exempt
def add_product(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def get_approval_status(request, bid_id):
    try:
        bid = Bids.objects.get(id=bid_id)
        serializer = BidsSerializer(bid)
        return Response({'status': serializer.data['is_approved'] == 'yes'})
    except Bids.DoesNotExist:
        return Response({'status': False, 'error': 'Bid not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@csrf_exempt
def get_user_types_list(request, user_id):
    try:
        user_instance = Users.objects.get(id=user_id)
        serializer = UsersSerializer(user_instance)
        return Response({"status": "success", "data": serializer.data['user_types']})
    except Users.DoesNotExist:
        return Response({"status": "error", "message": f"User with id {user_id} does not exist"}, status=404)
    

@api_view(['POST'])
@csrf_exempt
def referral(request):
    
    serializers = ReferralSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def changeBidWinUser(request):
    bid_id = request.data.get('bid_id', None)
    party2_id = request.data.get('party2_id', None)
    party2_name = request.data.get('party2_name', None)

    if not bid_id or not party2_id or not party2_name:
        return Response({"error": "bid_id, party2_id and party2_name are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        bid_instance = Bids.objects.get(id=bid_id)
    except Bids.DoesNotExist:
        return Response({"error": "Bid not found"}, status=status.HTTP_404_NOT_FOUND)

    bid_instance.party2_id = party2_id
    bid_instance.party2_name = party2_name
    bid_instance.save()

    serializer = BidsSerializer(bid_instance)

    return Response(serializer.data, status=status.HTTP_200_OK)
      

@api_view(['GET'])
@csrf_exempt
def get_domains(request):
    domains = Domains.objects.all().values()
    return Response({"status": "success", "data": domains})


@api_view(['GET'])
@csrf_exempt
def get_users_types(request):
    user_types = UserType.objects.all().values()
    return Response({"status": "success", "data": user_types})


@api_view(['GET'])
@csrf_exempt
def get_approve_users_types(request):
    user_types = UserType.objects.filter(is_approved='yes').values()

    final_list=[]
    for i in user_types:
        final_list.append(i.get('name'))
        
    return Response({"status": "success", "data": final_list})


@api_view(['GET'])
@csrf_exempt
def get_approve_users(request):
    users = Users.objects.filter(is_approved='yes').values()
    return Response({"status": "success", "data": users})


@api_view(['GET'])
@csrf_exempt
def get_unapprove_users(request):
    users = Users.objects.filter(is_approved='no').values()
    return Response({"status": "success", "data": users})


@api_view(['GET'])
@csrf_exempt
def get_approved_domains(request):
    domains = Domains.objects.filter(is_approved='yes').values()

    print(domains)
    final_list=[]
    for i in domains:
        final_list.append(i.get('name'))

    return Response({"status": "success", "data": final_list})


@api_view(['GET'])
@csrf_exempt
def get_unapproved_domains(request):
    domains = Domains.objects.filter(is_approved='no').values()
    return Response({"status": "success", "data": domains})


@api_view(['GET'])
@csrf_exempt
def get_approved_products(request):
    products = Products.objects.filter(is_approved='yes').values()
    return Response({"status": "success", "data": products})


@api_view(['GET'])
@csrf_exempt
def get_unapproved_products(request):
    products = Products.objects.filter(is_approved='no').values()
    return Response({"status": "success", "data": products})


@api_view(['GET'])
@csrf_exempt
def get_banner(request):
    banners = Banner.objects.all().values()
    return Response({"status": "success", "data": banners})
