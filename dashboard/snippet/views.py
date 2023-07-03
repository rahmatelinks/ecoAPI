from django.http import HttpResponse
from django.shortcuts import render
from snippet.models import Add_apis

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def reset_password(request):
    return render(request, 'reset-password.html')

def docs(request):
    return render(request, 'docs.html')

# -------APIS------
def apis(request):
    take_api = Add_apis.objects.all()
    return render(request, 'apis.html', {'final_api': take_api})

def create_api(request):
    return render(request, 'create_api.html')

def single_api_details(request):
    take_api = Add_apis.objects.all()
    return render(request, 'single_api_details.html', {'final_api': take_api})
# --------------

def charts(request):
    return render(request, 'charts.html')

def settings(request):
    return render(request, 'settings.html')

def help_page(request):
    return render(request, 'help.html')

def account(request):
    return render(request, 'account.html')

def notifications(request):
    return render(request, 'notifications.html')

def error_page(request):
    return render(request, '404.html')





