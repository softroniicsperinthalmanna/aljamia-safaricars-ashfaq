from django.shortcuts import render,redirect,get_list_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate , logout 
from django.contrib import messages
from . forms import UserRegistrationForm
from . forms import SellcarForm,fbForm,addressForm,testForm,serviceForm
from django .views import View
from .models import *
#activation of email
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.contrib.sites.shortcuts import get_current_site
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth.views import PasswordResetConfirmView
# from django.contrib.sites.shortcuts import get_current_site
# from django.urls import reverse_lazy
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.utils.decorators import method_decorator
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.generic import CreateView, TemplateView
# from django.core.mail import EmailMessage

#end
# Create your views here.
def index(request):
   laxury_cars= l_cars.objects.all()
   laxury_bikes= l_bikes.objects.all()
   product= dis_product.objects.all()


   return render(request,'index.html',locals())
def  acc(request):
    #search
    if 'q' in request.GET:
        q=request.GET['q']
        acc=add_product.objects.filter(p_name__icontains=q)
    else:
           acc= add_product.objects.all()

    return render(request,'acc.html',locals())
# def  sellcar(request):
#     form=SellcarForm
#     return render(request,'sellcar.html',locals())
class SellCarView(View):
    def get(self,request):
        form=SellcarForm
        return render (request,'sellcar.html', locals()) 
    def post(self,request): 
        form=SellcarForm(request.POST, request.FILES)  
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name'] 
            mobile=form.cleaned_data['mobile'] 
            email=form.cleaned_data['email'] 
            brand=form.cleaned_data['brand'] 
            model=form.cleaned_data['model'] 
            year=form.cleaned_data['year'] 
            km_driven=form.cleaned_data['km_driven'] 
            mailage=form.cleaned_data['mailage'] 
            Color=form.cleaned_data['Color'] 
            no_owner=form.cleaned_data['no_owner']
            engine_CC=form.cleaned_data['engine_CC']
            insurence_validity=form.cleaned_data['insurence_validity']
            year_of_registration=form.cleaned_data['year_of_registration']
            transmisson=form.cleaned_data['transmisson']
            fuel=form.cleaned_data['fuel']
            discription=form.cleaned_data['discription']
            image=form.cleaned_data['image']
            parking_sensor = form.cleaned_data['parking_sensor']
            center_lock = form.cleaned_data['center_lock']
            Rear_camera = form.cleaned_data['Rear_camera']
            Navigation_system = form.cleaned_data['Navigation_system']
            Adjustable_stearing = form.cleaned_data['Adjustable_stearing']
            reg=sell_your_car( user= user, name = name, mobile= mobile, email=email, brand= brand,  model= model,
                              year= year, km_driven=km_driven, mailage=mailage, Color= Color, no_owner=no_owner, 
                              engine_CC=engine_CC, insurence_validity=insurence_validity, year_of_registration=year_of_registration,
                              transmisson=transmisson, fuel=fuel, discription=discription,
                              image=image,parking_sensor=parking_sensor,center_lock=center_lock,Rear_camera=Rear_camera,
                              Navigation_system=Navigation_system,Adjustable_stearing=Adjustable_stearing)
            reg.save()
            messages.success(request, "congratulations!! your vehicle details added successfully")
            return redirect('sellcar')
        else:
           messages.warning(request,"Invalid input data")  
      
        return render (request,'sellcar.html', locals())



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
    
def  car(request,pk):
     #preview
    car = l_cars.objects.get(id=pk)
    context={'cars':car}

    return render(request,'car.html',{'car':car})
def  car1(request,pk):
     #preview
    bike = l_bikes.objects.get(id=pk)
    context={'bikes':bike}
    return render(request,'car1.html',{'bike':bike})
def  car2(request,pk):
     #preview
    car = add_vehicle.objects.get(id=pk)
    context={'cars':car}
    return render(request,'car2.html',{'car':car})

class serviceView(View):
     def get(self,request):
        form=serviceForm
        return render(request,'service.html',locals())
     def post(self,request):
        form=serviceForm(request.POST, request.FILES)  
        if form.is_valid():
            user=request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            car=form.cleaned_data['car']
            brand=form.cleaned_data['brand']
            reg_no=form.cleaned_data['reg_no']
            serv=form.cleaned_data['serv']
            deliv=form.cleaned_data['deliv']
            date=form.cleaned_data['date']
            # form.save()
            reg=service(user=user,name=name,mobile= mobile, email=email, car= car,brand=brand, reg_no=reg_no,serv=serv,deliv=deliv,date=date)   
            reg.save()
            messages.success(request, " your servic has been booked successfully")
            return redirect('service')
        else:
           messages.warning(request,"Invalid input data")  
      
        return render (request,'service.html', locals())

def  gar(request):
    gar= add_garage.objects.all()

    return render(request,'gar.html',locals())
def  ad(request):
    ad= add_featre_ad.objects.all()

    return render(request,'ad.html',locals())

class feedbackView(View):
    def get(self,request):
        form=fbForm
        return render(request,'fb.html',locals())
    def post(self,request):
        form=fbForm(request.POST, request.FILES)  
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name'] 
            mobile=form.cleaned_data['mobile'] 
            email=form.cleaned_data['email'] 
            message=form.cleaned_data['message'] 
            reg=feedback(user=user,name=name,mobile= mobile, email=email, message= message)   
            reg.save()
            messages.success(request, "congratulations!! your feedback is added successfully")
            return redirect('fb')
        else:
           messages.warning(request,"Invalid input data")  
      
        return render (request,'fb.html', locals())

    

class testView(View):
    def get(self,request):
        form=testForm
        return render(request,'test.html',locals())
    def post(self,request):
        form=testForm(request.POST, request.FILES)  
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name'] 
            mobile=form.cleaned_data['mobile'] 
            email=form.cleaned_data['email'] 
            date=form.cleaned_data['date'] 
            time=form.cleaned_data['time'] 
            form.save()
            messages.success(request, " your Address has been registerd successfully")
            return redirect('test')
        else:
           messages.warning(request,"Invalid input data")  
      
        return render (request,'test.html', locals())
    


class addressView(View):
    def get(self,request):
        form=addressForm
        return render(request,'adress.html',locals())
    def post(self,request):
        form=addressForm(request.POST, request.FILES)  
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name'] 
            mobile=form.cleaned_data['mobile'] 
            email=form.cleaned_data['email'] 
            address=form.cleaned_data['address'] 
            city=form.cleaned_data['city'] 
            district=form.cleaned_data['district'] 
            pincode=form.cleaned_data['pincode'] 
            # reg=address(user=user,name=name,mobile= mobile, email=email,address=address,city=city,district=district,pincode=pincode)  
           
            # reg.save()
            form.save()
            messages.success(request, " your Address has been registerd successfully")
            return redirect('adress')
        else:
           messages.warning(request,"Invalid input data")  
      
        return render (request,'adress.html', locals())
    
    
#activation of email

# def activate(request,uidb64,token):
#      context = {'uidb64':uidb64, 'token':token}
#      return redirect('home',context)

# def activateEmail(request,user,to_email):
#     mail_subject ="Activate user account"
#     message=render_to_string("reg.html",{
#         'user':user.username,
#         'domain':get_current_site(request).domain,
#         'uid':urlsafe_base64_decode(force_bytes(user.pk)),
#         'token':account_activation_token.make_token(user),
#         "protocol":'https' if request.is_secure() else 'http'
        
#     })
#     email=EmailMessage(mail_subject,message,to=[to_email])
#     if email.send():
        
#         messages.success(request,f'Dear <b>{user}</b>,please go to Email <b>{to_email}</b> inbox and click on recived activation link to confirm and complete the registarion <b>note</b> Check spam folder')
#     else:
#         messages.error(request,f'problem sending email to {to_email},check if you typed correctly.')
# @user_not_authenticated
#end
def reg(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                # user = form.cleaned_data.get('username')
                #activation of email
                # activateEmail(request,User,form.cleaned_data.get('email'))
                #end
                messages.success(request, 'Your account has been created. You can log in now!')    
                return redirect('login')
        else:
            form = UserRegistrationForm()

        context = {'form': form}
        return render(request, 'reg.html', context)





def  otp(request):
    return render(request,'otp.html')
def  contact(request):
    return render(request,'contact.html')


def  product(request,pk):
    #preview
    product = dis_product.objects.get(id=pk)
    context={'products':product}

    return render(request,'product.html',{'product':product})
def  product2(request,pk):
    #preview
    product = add_product.objects.get(id=pk)
    context={'products':product}

    return render(request,'product2.html',{'product':product})


def  cart(request):
    return render(request,'cart.html')
def  order_details(request):
    return render(request,'order_details.html')
def  servicedt(request):
    ser= service.objects.filter(user=request.user)

    return render(request,'servicedt.html',locals())

def testdrivedetails(request):
    tst=test.objects.filter(user=request.user)
    
    return render(request,'testdrivedetails.html',locals())


def  cars(request):
     #search
    if 'q' in request.GET:
        q=request.GET['q']
        car=add_vehicle.objects.filter(brand__icontains=q)
    else:
        car= add_vehicle.objects.all()
    
    #dropdown
    if 'dropdown' in request.GET:
        dropdown=request.GET['dropdown']
        car=add_vehicle.objects.filter(fuel__icontains=dropdown)
    else:
        car= add_vehicle.objects.all()
        
    if 'transmisson' in request.GET:
        transmisson=request.GET['transmisson']
        car=add_vehicle.objects.filter(transmisson__icontains=transmisson)
    else:
        car= add_vehicle.objects.all()


    return render(request,'cars.html',locals())
  
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