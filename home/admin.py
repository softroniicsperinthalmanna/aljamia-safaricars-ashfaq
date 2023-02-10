from django.contrib import admin
from . models import sell_your_car,feedback,address,test,service
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
    