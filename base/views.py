from django.shortcuts import render
from django.http import HttpResponse
import io

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def index(request):
    return render(request, 'base/index.html')
