from django.shortcuts import render, get_object_or_404
from apis.models import Users, Bids, Assessment
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import DynamicAssessmentForm

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

def create_assessment(request):
    if request.method == 'POST':
        # Process dynamic data and convert it to JSON
        dynamic_data = {}
        for key, value in request.POST.items():
            if key.startswith('data_key_') and value:
                field_number = key.split('_')[-1]
                data_key = value
                data_value = request.POST.get(f'data_value_{field_number}')
                dynamic_data[data_key] = data_value

        Assessment.objects.create(data=dynamic_data)
        return redirect('/')  # Redirect to the assessment list vie

    return render(request, 'create_assessment.html')

def edit_assessment(request, assessment_id):
    assessment = Assessment.objects.get(pk=assessment_id)
    form_data = {}
    for i, (key, value) in enumerate(assessment.data.items()):
        form_data['data_key_{}'.format(i)] = key
        form_data['data_value_{}'.format(i)] = value

    form = DynamicAssessmentForm(initial=form_data)

    if request.method == 'POST':
        dynamic_data = {}
        for key, value in request.POST.items():
            if key.startswith('data_key_') and value:
                field_number = key.split('_')[-1]
                data_key = value
                data_value = request.POST.get(f'data_value_{field_number}')
                dynamic_data[data_key] = data_value

        assessment.data = dynamic_data
        assessment.save()
        return redirect('/')  # Redirect to the assessment list view

    return render(request, 'edit_assessment.html', {'data': form_data, 'form': form})
