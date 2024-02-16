from django.shortcuts import render, get_object_or_404
from apis.models import Users, Bids
from django.http import JsonResponse

def dashboard(request):
    # Get the count of all users
    user_count = Users.objects.count()

    # Get the count of users based on user_type
    supplier_count = Users.objects.filter(user_type='supplier').count()
    manufacturer_count = Users.objects.filter(user_type='manufacturer').count()
    referral_count = Users.objects.filter(user_type='referral').count()

    bid_count = Bids.objects.count()

    on_going_bid_count= Bids.objects.filter(bid_status='on_going').count()
    bid_finished_count = Bids.objects.filter(bid_status='finished').count()
    bid_cancelled_count = Bids.objects.filter(bid_status='cancelled').count()

    return render(request, 'dashboard.html', {
        'user_count': user_count,
        'bid_count': bid_count,
        'supplier_count': supplier_count,
        'manufacturer_count': manufacturer_count,
        'referral_count': referral_count,
        "bid_cancelled_count": bid_cancelled_count,
        "on_going_bid_count": on_going_bid_count,
        "bid_finished_count": bid_finished_count
    })

def users_by_type_view(request):
    user_type = request.GET.get('user_type', '')        # params
    users = Users.objects.filter(user_type=user_type)

    return render(request, 'users.html', {'users': users, 'user_type': user_type})

def bids_by_type_view(request):
    bid_type = request.GET.get('bid_type', '')  # Assuming bid_type is a field in your Bids model
    bids = Bids.objects.filter(bid_type=bid_type)

    return render(request, 'bids.html', {'bids': bids, 'bid_type': bid_type})


def bids_view(request):
    bids = Bids.objects.all()

    return render(request, 'bids.html', {'bids': bids})

def bids_edit_view(request):    
    bid_id = request.GET.get('id', '')        # params
    bid = Bids.objects.filter(id=bid_id)

    if request.method == "POST":
            bid_id = request.POST.get('id')
            bid = get_object_or_404(Bids, id=bid_id)

            bid.item = request.POST.get('item')
            bid.description = request.POST.get('description')
            bid.price = request.POST.get('price') 
            bid.bid_type = request.POST.get('bid_type')
            bid.bid_category = request.POST.get('bid_category')
            bid.bid_sub_category = request.POST.get('bid_sub_category')
            bid.bid_opening_time = request.POST.get('bid_opening_time')
            bid.bid_closing_time = request.POST.get('bid_closing_time')

            bid.save()  

            bid_id = request.GET.get('id', '')       
            bid = Bids.objects.filter(id=bid_id)
            return render(request, 'editbid.html', {'bid_data': bid, 'bid_id': bid_id})

    return render(request, 'editbid.html', {'bid_data': bid, 'bid_id': bid_id})

def toggle_approval(request, bid_id):
    try:
        print(bid_id)
        bid = Bids.objects.get(id=bid_id)
        bid.is_approved = 'no' if bid.is_approved == 'yes' else 'yes'
        bid.save()
        return JsonResponse({'status': 'success', 'is_approved': bid.is_approved})
    except Bids.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Bid not found'}, status=404)
