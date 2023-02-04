from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def index(request):
    return render(request,'index.html')
def  acc(request):
    return render(request,'acc.html')
def  sellcar(request):
    return render(request,'sellcar.html')
def  log(request):
        if request.method == 'POST':
             username = request.POST.get('username')
             password = request.POST.get('password')

             user = authenticate(request, username=username, password=password)
             if user is not None:
                 login(request, user)
                 return redirect('home')
             else:
                 messages.info(request, 'Username or password is incorrect')

        context ={}
        return render (request, 'log.html', context)
    
def  logout(request):
    logout(request)
    return redirect(login)
    
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
def  adress(request):
    return render(request,'adress.html')
def reg(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                # user = form.cleaned_data.get('username')
                messages.success(request, 'Your account has been created. You can log in now!')    
                return redirect('login')
        else:
            form = UserRegistrationForm()

        context = {'form': form}
        return render(request, 'reg.html', context)





def  otp(request):
    return render(request,'otp.html')
def  product(request):
    return render(request,'product.html')
def  cart(request):
    return render(request,'cart.html')
def  order_details(request):
    return render(request,'order_details.html')
def  servicedt(request):
    return render(request,'servicedt.html')
def testdrivedetails(request):
    return render(request,'testdrivedetails.html')
def  cars(request):
    return render(request,'cars.html')
  
    #<------------- admin------------------------------>
# def  a_index(request):
#     return render(request,'a_index.html')
# def  a_reg(request):
#     return render(request,'a_reg.html')
# def  a_accessories(request):
#     return render(request,'a_accessories.html')
# def  a_add_feature_ad(request):
#     return render(request,'a_add_feature_ad.html')
# def  a_add_product(request):
#     return render(request,'a_add_product.html')
# def  a_add_vehicle(request):
#     return render(request,'a_add_vehicle.html')
# def  a_car_info(request):
#     return render(request,'a_car_info.html')
# def  a_car_req(request):
#     return render(request,'a_car_req.html')
# def  a_customers(request):
#     return render(request,'a_customers.html')
# def  a_dash(request):
#     return render(request,'a_dash.html')