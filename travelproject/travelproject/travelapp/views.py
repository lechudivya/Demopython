from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"demo.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("hello am contact")