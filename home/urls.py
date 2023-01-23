from django.contrib import admin
from django.urls import path,include
from  . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('accessories/',views.acc,name='acc'),
    path('sellyourcar/',views.sellcar,name='sellcar'), 
    path('login/',views.log,name='login'),   
    path('cars/',views.car,name='car'), 
    path('service/',views.service,name='service'),   
    path('garage/',views.gar,name='gar'),
    path('feedback/',views.fb,name='fb'),
    path('testdrive/',views.test,name='test'),
    path('register/',views.reg,name='reg'),
    path('OTP/',views.otp,name='otp'),
    path('product/',views.product,name='product'),





  
]