from django.contrib import admin
from . models import sell_your_car,feedback,address,test,service,add_vehicle,add_product,l_cars,l_bikes,add_featre_ad,add_garage
# Register your models here.
@admin.register(sell_your_car)
class  sell_your_carModelAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email','brand','model','year','km_driven','mailage','Color','no_owner','engine_CC','insurence_validity','year_of_registration','transmisson','fuel','discription','image','parking_sensor','Rear_camera','Navigation_system','Adjustable_stearing']
@admin.register(feedback)
class  feedbackModelAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email','message']
@admin.register(address)
class  ModelAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email','address','city','district','pincode']
@admin.register(test)
class testModelAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email','date','time']
@admin.register(service)
class serviceModelAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email','car','brand','reg_no','serv','deliv','date']
@admin.register(add_vehicle)
class add_vehicleModelAdmin(admin.ModelAdmin):
    list_display=['brand','model','year','km_driven','mailage','Color','no_owner','engine_CC','insurence_validity','year_of_registration','transmisson','fuel','discription','image','parking_sensor','Rear_camera','Navigation_system','Adjustable_stearing','c_price']
@admin.register(add_product)
class add_productModelAdmin(admin.ModelAdmin):
    list_display=['p_name','p_price','discription','image']
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