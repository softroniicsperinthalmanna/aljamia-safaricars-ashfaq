from django.contrib import admin
# from . models import SELL_CAR,Address,Service,Feedback,Test_drive,add_vehicle,add_product,l_cars,l_bikes,add_featre_ad,add_garage
# # Register your models here.
from . models import *
@admin.register(SELL_CAR)
class  SELL_CARModelAdmin(admin.ModelAdmin):
    list_display=['id','name','mobile','email','brand','model','year','km_driven','mileage','color','No_of_owners','engine_cc','Insurance_validity','year_of_registration','mode_of_transmission','type_of_vehicle','vehicle_images','extras']

@admin.register(Address)
class  AddressModelAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_number','email','address','city','state','pincode']

@admin.register(Service)
class  ServiceModelAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_number','email','car_model','brand','reg_no','type_of_service','mode_of_vehicle_taking','service_booked_on']

@admin.register(Feedback)
class  FeedbackModelAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_number','message',] 
    readonly_fields = ['id','name','phone_number','message',]
    
    def has_add_permission(self, request):
      return False

    def has_delete_permission(self, request, obj=None):
      return False


@admin.register(Test_drive)
class  Test_driveModelAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_number','email','vehicle_name','select_date','select_time']     

# class MyModelForm(forms.ModelForm):

# class Meta:
#     model = MyModel
#     fields = '__all__'


# class MyModelAdmin(admin.ModelAdmin):
#     form = QuestionTrackAdminForm
#     list_display = ['title', 'weight']
#     readonly_fields = ['title', 'weight']

# admin.site.register(MyModel, MyModelAdmin)       

@admin.register(add_vehicle)
class add_vehicleModelAdmin(admin.ModelAdmin):
    list_display=['brand','model','year','km_driven','mailage','Color','no_owner','engine_CC','insurence_validity','year_of_registration','transmisson','fuel','discription','image','parking_sensor','Rear_camera','Navigation_system','Adjustable_stearing','c_price']
@admin.register(add_product)
class add_productModelAdmin(admin.ModelAdmin):
    list_display=['id','p_name','p_price','discription','image']
@admin.register(l_cars)
class l_carsModelAdmin(admin.ModelAdmin):
    list_display=['l_brand','l_model','l_year','l_km_driven','l_Color','l_no_owner','l_engine_CC','l_insurence_validity','l_transmisson','l_fuel','l_discription','l_image','l_price']
@admin.register(l_bikes)
class l_bikesModelAdmin(admin.ModelAdmin):
    list_display=['b_brand','b_model','b_year','b_km_driven','b_Color','b_no_owner','b_engine_CC','b_insurence_validity','b_transmisson','b_fuel','b_discription','b_image','b_price']
@admin.register(add_featre_ad)
class add_featre_adModelAdmin(admin.ModelAdmin):
    list_display=['f_image']
@admin.register(add_garage)
class add_garageModelAdmin(admin.ModelAdmin):
    list_display=['place','mobile','g_image','g_discription']

@admin.register(Cart)
class  CartModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'product','quantity']


@admin.register(Payment)
class  PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class  OrderPlacedtModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'customer','product','quantity','ordered_date','status','payment']

