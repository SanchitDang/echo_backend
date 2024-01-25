from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    admins = [
        {'name':'admin', 'pass':'123456'},
        {'name':'admin2', 'pass':'123456'}
    ]
    return render(request, 'dashboard/index.html', context = { 'admins' : admins, 'name' : "hahaha" })