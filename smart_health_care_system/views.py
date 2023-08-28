from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is homepage of smart_health_care_system")