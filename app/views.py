from django.shortcuts import render
from django.http import HttpResponse
from app.models import Bio

# Create your views here.
def index(request):
    key=Bio.objects.all()
    return render(request, "index.html", {'data':key})

def detail(request):
    Detl=Bio.objects.all()
    return render(request, "detail.html",{'details':Detl})
        
