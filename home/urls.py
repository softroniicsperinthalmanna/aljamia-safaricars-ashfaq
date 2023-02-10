from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from  . import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='log.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name='logout.html'),name='logout'),
    path('reg/', views.reg, name='reg'),
    
    
    path('',views.index,name='home'),
    path('accessories/',views.acc,name='acc'),
    path('sellyourcar/',views.SellCarView.as_view(),name='sellcar'), 
    

    path('car/',views.car,name='car'), 
    path('service/',views.serviceView.as_view(),name='service'),   
    path('garage/',views.gar,name='gar'),
    path('feedback/',views.feedbackView.as_view(),name='fb'),
    
    path('testdrive/',views.testView.as_view(),name='test'),
    path('OTP/',views.otp,name='otp'),
    path('product/',views.product,name='product'),
    path('adress/',views.addressView.as_view(),name='adress'),
    path('cart/',views.cart,name='cart'),
    path('order_details/',views.order_details,name='order_details'),
    path('servicedt/',views.servicedt,name='servicedt'),
    path('testdrivedetails/',views.testdrivedetails,name='testdrivedetails'),
    path('cars/',views.cars,name='cars'), 

    #<------------- admin------------------------------>

    # path('admin/',admin.site.urls),
    #<------------- admin------------------------------>
    # path('a_index/',views.a_index,name='a_log'),
    # path('a_reg/',views.a_reg,name='a_register'),
    # path('a_accessories/',views.a_accessories,name='a_accessories'),
    # path('a_add_feature_ad/',views.a_add_feature_ad,name='a_add_feature_ad'),
    # path('a_add_product/',views.a_add_product,name='a_add_product'),
    # path('a_add_vehicle/',views.a_add_vehicle,name='a_add_vehicle'),
    # path('a_car_info/',views.a_car_info,name='a_car_info'),
    # path('a_car_req/',views.a_car_req,name='a_car_req'),
    # path('a_customers/',views.a_customers,name='a_customers'),
    # path('a_dash/',views.a_dash,name='a_dash'),
    # path('a_order/',views.a_order,name='a_order'),
    # path('a_vehicle/',views.a_vehicle,name='a_vehicle'),
    # path('a_product/',views.a_product,name='a_dash'),
    # path('a_dash/',views.a_dash,name='a_dash'),


  


   





  
]