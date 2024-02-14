from django.shortcuts import render
from apis.models import Users, Bids

def dashboard(request):
    # Get the count of all users
    user_count = Users.objects.count()

    # Get the count of users based on user_type
    supplier_count = Users.objects.filter(user_type='supplier').count()
    manufacturer_count = Users.objects.filter(user_type='manufacturer').count()
    referral_count = Users.objects.filter(user_type='referral').count()

    bid_count = Bids.objects.count()

    # bid_live_count = Bids.objects.filter(bid_status='').count()
    # bid_finished_count = Bids.objects.filter(bid_status='').count()
    # bid_cancelled_count = Bids.objects.filter(bid_status='').count()

    return render(request, 'dashboard.html', {
        'user_count': user_count,
        'bid_count': bid_count,
        'supplier_count': supplier_count,
        'manufacturer_count': manufacturer_count,
        'referral_count': referral_count,
    })

def users_by_type_view(request):
    user_type = request.GET.get('user_type', '')
    users = Users.objects.filter(user_type=user_type)

    return render(request, 'users.html', {'users': users, 'user_type': user_type})

def bids_by_type_view(request):
    bid_type = request.GET.get('bid_type', '')  # Assuming bid_type is a field in your Bids model
    bids = Bids.objects.filter(bid_type=bid_type)

    return render(request, 'bids.html', {'bids': bids, 'bid_type': bid_type})


def bids_view(request):
    bids = Bids.objects.all()

    return render(request, 'bids.html', {'bids': bids})