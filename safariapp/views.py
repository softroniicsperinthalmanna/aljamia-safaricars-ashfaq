from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from django.views import View
from . models import *
from django.http import JsonResponse
from django.db.models import Q
# from django.shortcuts import render_to_response
# from django.template.context import RequestContext
#from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .tokens import account_activation_token
from .forms import SetPasswordForm,PasswordResetForm
from django.db.models.query_utils import Q
# from decorators import user_not_authenticated
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User
from django.views.generic import TemplateView
# from django.utils.encoding import force_bytes, force_text 
from django.utils.encoding import force_str
import razorpay
# from django.contrib.auth.decorators import login_required
# from shopping_cart.extras import generate_order_id, transact, generate_client_token
# Create your views here.

# class index(View):
#     def post(self, request):
#         prod=request.POST.get('prod')
#         # print(product)
#         cart= request.session.get('cart')
#         if cart:
#             quantity=cart.get(prod)
#             if quantity:
#               cart[prod]=quantity+1

#             else:
#                 cart[prod]=1  
#         else:
#            cart={}
#            cart[prod]=1

#         request.session['cart']=cart
#         print('cart',request.session['cart'])
#         return redirect('home')

#     def get(self, request):
#         products=None
#         # request.session.get('cart').clear()
#         laxury_cars=l_cars.objects.all()
#         laxury_bikes=l_bikes.objects.all()
#         Accessories=add_product.objects.all()
#         return render (request,'user/index.html',locals())

    




def index(request):
    # products=Product.objects.get_all()
    laxury_cars=l_cars.objects.all()
    laxury_bikes=l_bikes.objects.all()
    Accessories=add_product.objects.all()
    # list = l_cars.objects.order_by('l_model')
    # context = {'cars':laxury_cars,'bikes':laxury_bikes }


    return render (request,'user/index.html',locals())

# def car_prvw(request):
class car_prvw(View):
   def get(self,request, pk):
      laxury_cars= l_cars.objects.get(pk=pk)
    #   laxury_bikes=l_bikes.objects.get(pk=pk)
    #   context = {'cars':car,'bikes':bike }
#     # products=Product.objects.filter(category=val).values_list('title', 'product_image','discounted_price') #flat=True)
#        products= add_product.objects.filter(category=val)
#        title = add_product.objects.filter(category=val).values('p_name')
      return render (request,'user/carpre.html', locals())

class bike_prvw(View):
   def get(self,request, pk):
    #   laxury_cars= l_cars.objects.get(pk=pk)
      laxury_bikes=l_bikes.objects.get(pk=pk) 
      return render (request,'user/bikepre.html', locals())     
# class CarPreviewTitle(View):
#   def get(self,request, val):
#      products= add_product.objects.filter(title=val)
#      title = add_product.objects.filter(category=products[0].category).values('p_name')
#      return render (request,'user/carpre.html', locals())

# class ProductDetail(View):
#    def get(self,request, pk):
#        products= add_product.objects.get(pk=pk)
#        return render (request,'user/carpre.html', locals())


def accessories(request):
    return render (request,'user/acc.html')

# def sellcar(request):
#     return render (request, 'user/sellcar.html')    

def service(request):
     if request.method == 'POST':
       form = ServiceForm(request.POST or None)
    #    my_Address = Address.objects.all()
       
       

       if form.is_valid():
           instance = form.save(commit=False)
           instance.name = form.cleaned_data.get("name")
           instance.phone_number = form.cleaned_data.get("phone_number")
           instance.message = form.cleaned_data.get("email")
           instance.car_model = form.cleaned_data.get("car_model")
           instance.brand= form.cleaned_data.get("brand")
           instance.reg_no= form.cleaned_data.get("reg_no")
           instance.type_of_service= form.cleaned_data.get("type_of_service")
           instance.mode_of_vehicle_taking= form.cleaned_data.get("mode_of_vehicle_taking")
           instance.service_booked_on= form.cleaned_data.get("service_booked_on")
           instance.user = request.user

           instance.save()
           messages.success(request, f'Address Added successfully')
        #    messages.success(request, messages.INFO,'Address Added')
           form = ServiceForm()
           
     else:
       messages.warning(request,'Invalid data')
       form = ServiceForm()
       
     return render (request,'user/service.html',{'form':form})  

def garage(request):
    return render (request,'user/gar.html')      

def feeds(request):
    if request.method == 'POST':
       form = FeedbackForm(request.POST or None)
    #    my_Address = Address.objects.all()
       
       

       if form.is_valid():
           instance = form.save(commit=False)
           instance.name = form.cleaned_data.get("name")
           instance.phone_number = form.cleaned_data.get("phone_number")
           instance.message = form.cleaned_data.get("message")
           instance.user = request.user

           instance.save()
           messages.success(request, f'Feedback Added successfully')
        #    messages.success(request, messages.INFO,'Address Added')
           form = FeedbackForm()
           
    else:
       messages.warning(request,'Invalid data')
       form = FeedbackForm()
    return render (request,'user/fb.html',{'form':form})       

# def login(request):
#     return render (request,'user/log.html')     

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid(): 
           user = form.save(commit=False)  
           user.is_active = False  
           user.save()  
    #         # to get the domain of the current site  
           current_site = get_current_site(request)  
           mail_subject = 'Activation link has been sent to your email id'  
           message = render_to_string('user/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
             })  
           to_email = form.cleaned_data.get('email')  
           email = EmailMessage(  
                         mail_subject, message, to=[to_email]  
            )  
           email.send()  
           return HttpResponse('Please confirm your email address to complete the registration, A verification link has been sent to your registered mail-id. Please check it')  
    else:  
      form = UserRegistrationForm()  
    return render(request, 'user/reg.html', {'form': form})  


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  
    #   form.save()

    #         messages.success(request, f'Your account has been created. You can log in now!')    
    #         return redirect('login')
    # else:
    #     form = UserRegistrationForm()

    # context = {'form': form}
    # return render (request,'user/reg.html',context)  

def otp(request):
    return render (request,'user/otp.html') 

def seemore (request):
    return render (request,'user/cars.html')   

# def social(request):
#    context = RequestContext(request,
#                            {'request': request,
#                             'user': request.user})
#    return render_to_response('reg.html',
#                              context_instance=context)
class SellCarView(View):
    def get(self,request):
        form=SellVehicleForm
        return render (request,'user/sellcar.html', locals()) 
    def post(self,request): 
        form=SellVehicleForm(request.POST, request.FILES)  
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name'] 
            mobile=form.cleaned_data['mobile'] 
            email=form.cleaned_data['email'] 
            brand=form.cleaned_data['brand'] 
            model=form.cleaned_data['model'] 
            year=form.cleaned_data['year'] 
            km_driven=form.cleaned_data['km_driven'] 
            mileage=form.cleaned_data['mileage'] 
            color=form.cleaned_data['color'] 
            No_of_owners=form.cleaned_data['No_of_owners']
            engine_cc=form.cleaned_data['engine_cc']
            Insurance_validity=form.cleaned_data['Insurance_validity']
            year_of_registration=form.cleaned_data['year_of_registration']
            mode_of_transmission=form.cleaned_data['mode_of_transmission']
            type_of_vehicle=form.cleaned_data['type_of_vehicle']
            vehicle_description=form.cleaned_data['vehicle_description']
            vehicle_images=form.cleaned_data['vehicle_images']
            extras=form.cleaned_data['extras']
            reg=SELL_CAR( user= user, name = name, mobile= mobile, email=email, brand= brand,  model= model,  year= year, km_driven=km_driven, mileage=mileage, color= color, No_of_owners=No_of_owners, engine_cc=engine_cc, Insurance_validity=Insurance_validity, year_of_registration=year_of_registration, mode_of_transmission=mode_of_transmission, type_of_vehicle=type_of_vehicle, vehicle_description=vehicle_description,vehicle_images=vehicle_images, extras=extras)
            reg.save()
            messages.success(request, "congratulations!! your vehicle details added successfully")
            return redirect('sell_car')
        else:
           messages.warning(request,"Invalid input data")  
      
        return render (request,'user/sellcar.html', locals())

def addressandcart(request):
    address=Address.objects.filter(user=request.user)
    if request.method == 'POST':
       form = UserAddressForm(request.POST or None)
    #    my_Address = Address.objects.all()
       
       

       if form.is_valid():
           instance = form.save(commit=False)
           instance.name = form.cleaned_data.get("name")
           instance.phone_number = form.cleaned_data.get("phone_number")
           instance.email = form.cleaned_data.get("email")
           instance.address = form.cleaned_data.get("address")
           instance.city= form.cleaned_data.get("city")
           instance.state= form.cleaned_data.get("state")
           instance.pincode= form.cleaned_data.get("pincode")
           instance.user = request.user

           instance.save()
           messages.success(request, f'Address Added successfully')
        #    messages.success(request, messages.INFO,'Address Added')
           form = UserAddressForm()
           
    else:
    #    messages.warning(request,'Invalid data')
       form = UserAddressForm()
       

    return render(request,'user/addressandcart.html',locals())  

class updateAddress(View):
    def get(self,request,pk):
        add=Address.objects.get(pk=pk)
        form=UserAddressForm(instance=add)
        return render(request,'user/updateAddress.html',locals())
    def post(self,request,pk):
        form=UserAddressForm(request.POST)
        if form.is_valid():
           add=Address.objects.get(pk=pk)
           add.name=form.cleaned_data['name'] 
        #    add.locality=form.cleaned_data['locality'] 
           add.city=form.cleaned_data['city'] 
           add. phone_number=form.cleaned_data['phone_number'] 
           add.state=form.cleaned_data['state'] 
           add.pincode=form.cleaned_data['pincode'] 
           add.save()
           messages.success(request, "congratulations!! profile updated successfully")
        else:
           messages.warning(request,"Invalid input data")      

        return redirect('user_address')     

def deleteAddress(request,pk):
    address=Address.objects.get(pk=pk)
    address.delete()
    return redirect('/user_address')



            
def test_drive(request):
     if request.method == 'POST':
       form = TestdriveForm(request.POST or None)
    #    my_Address = Address.objects.all()
       
       

       if form.is_valid():
           instance = form.save(commit=False)
           instance.name = form.cleaned_data.get("name")
           instance.phone_number = form.cleaned_data.get("phone_number")
           instance.email = form.cleaned_data.get("email")
           instance.vehicle_name = form.cleaned_data.get("vehicle_name")
           instance.select_date = form.cleaned_data.get("select_date")
           instance.select_time = form.cleaned_data.get("select_time")
           instance.user = request.user

           instance.save()
           messages.success(request, "Test drive opted successfully")
        #    messages.success(request, messages.INFO,'Address Added')
           form = TestdriveForm()
           
     else:
    #    messages.warning(request,'Invalid data')
       form = TestdriveForm()
     return render (request,'user/test.html',{'form':form})


# @login_required
# def password_change(request):
#     user = request.user
#     if request.method == 'POST':
#         form = SetPasswordForm(user, request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your password has been changed")
#             return redirect('login')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)

#     form = SetPasswordForm(user)
#     return render(request, 'password_reset_confirm.html', {'form': form})


# def password_reset_request(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             user_email = form.cleaned_data['email']
#             associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
#             if associated_user:
#                 subject = "Password Reset request"
#                 message = render_to_string("template_reset_password.html", {
#                     'user': associated_user,
#                     'domain': get_current_site(request).domain,
#                     'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
#                     'token': account_activation_token.make_token(associated_user),
#                     "protocol": 'https' if request.is_secure() else 'http'
#                 })
#                 email = EmailMessage(subject, message, to=[associated_user.email])
#                 if email.send():
#                     messages.success(request,
#                         """
#                         Password reset sent
                      
#                             We've emailed you instructions for setting your password, if an account exists with the email you entered. 
#                             You should receive them shortly.If you don't receive an email, please make sure you've entered the address 
#                             you registered with, and check your spam folder.
                        
#                         """
#                     )
#                 else:
#                     messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

#             return redirect('login')

#         for key, error in list(form.errors.items()):
#             if key == 'captcha' and error[0] == 'This field is required.':
#                 messages.error(request, "You must pass the reCAPTCHA test")
#                 continue

#     form = PasswordResetForm()
#     return render(
#         request=request, 
#         template_name="password_reset.html", 
#         context={"form": form}
#         )

# def passwordResetConfirm(request, uidb64, token):
#     User = get_user_model()
#     # var_username =  get_object_or_404(request.user)
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except:
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         if request.method == 'POST':
#             form = SetPasswordForm(user, request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Your password has been set. You may go ahead and log in  now.")
#                 return redirect('home')
#             else:
#                 for error in list(form.errors.values()):
#                     messages.error(request, error)

#         form = SetPasswordForm(user)
#         return render(request, 'password_reset_confirm.html', {'form': form})
#     else:
#         messages.error(request, "Link is expired")

#     messages.error(request, 'Something went wrong, redirecting back to Homepage')
#     return redirect("home")


# def order_details(request):
#     if request.method == 'POST':
#        form = OrderForm(request.POST or None)
#     #    my_Address = Address.objects.all()
       
       

#        if form.is_valid():
#            instance = form.save(commit=False)
#            instance.Your_name = form.cleaned_data.get("Your_name")
#            instance.Product = form.cleaned_data.get("Product")
#            instance.contact_number = form.cleaned_data.get("contact_number")
#            instance.Contact_info = form.cleaned_data.get("Contact_info")
#            instance.Quantity = form.cleaned_data.get("Quantity")
#            instance.user = request.user

#            instance.save()
#            messages.success(request, "Test drive opted successfully")
#         #    messages.success(request, messages.INFO,'Address Added')
#            form = OrderForm()
           
#     else:
#     #    messages.warning(request,'Invalid data')
#        form = OrderForm()
#     return render (request,'user/order_details.html',locals())  
    #  return render (request,'user/test.html',{'form':form})

      

def service_details(request):
    return render (request,'user/servicedetails.html')     

def test_details(request):
    return render (request,'user/testdrivedetails.html')   

def payment(request):
    return render (request,'user/paypal.html')       
        
# class CheckoutView(TemplateView):
#     template_name='user/checkout.html'

# def add_to_cart(request, **kwargs):
# @login_required()
# def add_to_cart(request, **kwargs):
#     # get the user profile
#     user_profile = get_object_or_404(Profile, user=request.user)
#     # filter products by id
#     product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
#     # check if the user already owns this product
#     if product in request.user.profile.ebooks.all():
#         messages.info(request, 'You already own this ebook')
#         return redirect(reverse('products:product-list')) 
#     # create orderItem of the selected product
#     order_item, status = OrderItem.objects.get_or_create(product=product)
#     # create order associated with the user
#     user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
#     user_order.items.add(order_item)
#     if status:
#         # generate a reference code
#         user_order.ref_code = generate_order_id()
#         user_order.save()

#     # show confirmation message and redirect back to the same page
#     messages.info(request, "item added to cart")
#     return redirect(reverse('products:product-list'))

def add_to_cart(request,pk):
   user=request.user
#    product_id=request.GET.get('prod_id')
#    product_id=request.GET.get('prod_id')
   product=add_product.objects.get(pk=pk)
   Cart(user=user, product=product).save()
#    return redirect('/cart')
   return redirect('showcart')

def show_cart(request):
    user=request.user
    # product_id=request.GET.get('prod_id')
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.p_price
        amount=amount + value
    totalamount = amount + 40    
    return render(request,'user/addtocart.html',locals())

class ProductDetail(View):
   def get(self,request, pk):
       products= add_product.objects.get(pk=pk)
       return render (request,'user/productdetail.html', locals())

class checkout(View):
    def get(self,request):
        user=request.user
        add=Address.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value = p.quantity * p.product.p_price
            famount = famount + value
        totalamount= famount + 40   
        razoramount=int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = { "amount":razoramount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment_response=client.order.create(data=data)
        print(payment_response)
        # {'id': 'order_LME7XitRGLAgd2', 'entity': 'order', 'amount': 1023000, 'amount_paid': 0, 'amount_due': 1023000, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1677666430}
        order_id=payment_response['id']
        order_status=payment_response['status']
        if order_status == 'created':
            payment=Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()

        return render(request,'user/checkout.html',locals())
@login_required
def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    print("payment_done : o_id=",order_id,"Pid=",payment_id,"cid=",cust_id)
    user=request.user
    customer=Address.objects.get(id=cust_id)
    print("success:",cust_id)
    # To update payment status and payment id
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid=True
    payment.razorpay_payment_id= payment_id
    payment.save()
    # To save order details
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()
    return redirect('orders')    





def plus_cart(request):
    if request.method == 'GET':
        # pk=request.GET['pk']
        # prod_id=request.GET['prod_id']
        pk=request.GET.get('pk')
        c=Cart.objects.get(Q(product=pk) & Q(user=request.user))
        # c=Cart.objects.get(Q(product=pk)& Q(user=request.user) )
        c.quantity +=1
        c.save()
        # print(pk)
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
           value=p.quantity * p.product.p_price
           amount=amount + value
        totalamount = amount + 40 
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }      
        return JsonResponse(data)
    

def minus_cart(request):
    if request.method == 'GET':
        # pk=request.GET['pk']
        # prod_id=request.GET['prod_id']
        pk=request.GET.get('pk')
        c=Cart.objects.get(Q(product=pk) & Q(user=request.user))
        # c=Cart.objects.get(Q(product=pk)& Q(user=request.user) )
        c.quantity -=1
        c.save()
        # print(pk)
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
           value=p.quantity * p.product.p_price
           amount=amount + value
        totalamount = amount + 40 
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }      
        return JsonResponse(data)    


def remove_cart(request):
    if request.method == 'GET':
        # pk=request.GET['pk']
        # prod_id=request.GET['prod_id']
        pk=request.GET.get('pk')
        c=Cart.objects.filter(Q(product=pk) & Q(user=request.user))
        # c=Cart.objects.get(Q(product=pk)& Q(user=request.user) )
        c.delete()
        
        # print(pk)
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
           value=p.quantity * p.product.p_price
           amount=amount + value
        totalamount = amount + 40 
        data={          
            'amount':amount,
            'totalamount':totalamount

        }      
        return JsonResponse(data)  

