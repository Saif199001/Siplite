
from django.shortcuts import render

def user_dashboard(request):
    return render(request, 'users/dashboard.html')
