from django.shortcuts import render
from django.http import HttpResponse
 

# Create your views here.
def index(request):
    return render(request,'index.html')
def  acc(request):
    return render(request,'acc.html')
def  sellcar(request):
    return render(request,'sellcar.html')
def  log(request):
    return render(request,'log.html')
def  car(request):
    return render(request,'car.html')
def  service(request):
    return render(request,'service.html')
def  gar(request):
    return render(request,'gar.html')
def  fb(request):
    return render(request,'fb.html')
def  test(request):
    return render(request,'test.html')
def  reg(request):
    return render(request,'reg.html')
def  otp(request):
    return render(request,'otp.html')
def  product(request):
    return render(request,'product.html')