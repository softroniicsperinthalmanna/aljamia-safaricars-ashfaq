from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user_name = models.CharField( max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)


GEAR =(
        ('automatic','AUTOMATIC'),
        ('manual','MANUAL')
)
FUEL= (
        ('petrol','PETROL'),
        ('deisel','DEISEL'),
        ('hybrid','HYBRID'),
        ('ev','ELECTRIC'),


)
   
class sell_your_car(models.Model):

     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     name = models.CharField(max_length=255,null=True)
     mobile = models.IntegerField()
     email = models.EmailField(max_length=255)
     brand= models.CharField(max_length=255)
     model= models.CharField(max_length=255)
     year= models.IntegerField()
     km_driven= models.IntegerField()
     mailage= models.IntegerField()
     Color= models.CharField(max_length=255)
     no_owner= models.IntegerField()
     engine_CC= models.CharField(max_length=255)
     insurence_validity= models.IntegerField()
     year_of_registration= models.IntegerField()
     transmisson= models.CharField(max_length=255, choices=GEAR, default='manual')
     fuel=models.CharField(max_length=255,choices=FUEL, default='petrol')
     discription=models.CharField(max_length=255)
     image = models.ImageField( max_length = 100)
     parking_sensor = models.BooleanField( "parking_sensor",default=False)
     center_lock = models.BooleanField( "center_lock",default=False)
     Rear_camera = models.BooleanField( "Rear_camera",default=False)
     Navigation_system = models.BooleanField( "Navigation_system",default=False)
     Adjustable_stearing = models.BooleanField( "Adjustable_stearing",default=False)

class feedback(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        name = models.CharField(max_length=255,null=True)
        mobile = models.IntegerField()
        email = models.EmailField(max_length=255)
        message = models.CharField(max_length=255)





class address(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        name = models.CharField(max_length=255,null=True)
        mobile = models.IntegerField()
        email = models.EmailField(max_length=255,null=True)
        address =  models.CharField(max_length=255,null=True)
        city =  models.CharField(max_length=255,null=True)
        district =  models.CharField(max_length=255,null=True)
        pincode =  models.IntegerField()


 
servic =(
          ('water service','WATER SERVICE'),
          ('running repair','RUNNING REPAIR'),
          ('Accessories fitiing','ACCESSORIES FITTING'),
          ('Paint & polish','PAINT & POLISH'),
          ('Oil change','OIL CHANGE'),
          ('others','OTHERS')
)   
delv =(
        ('pickup','PICKUP'),
        ('drop','DROP'),
        ('pick and drop','PICKUP AND DROP'),   
        ('not required','NOT REQUIRED')
)     
class service(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        name = models.CharField(max_length=255,null=True)
        mobile = models.IntegerField()
        email = models.EmailField(max_length=255)
        car=models.CharField(max_length=255)
        brand=models.CharField(max_length=255)
        reg_no=models.CharField(max_length=255)
        serv=models.CharField(max_length=255, choices=servic , default='water')#drop
        deliv=models.CharField(max_length=255,choices=delv , default='PICKUP')#drop
        date=models.DateField()
class test(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        name = models.CharField(max_length=255,null=True)
        mobile = models.IntegerField()
        email = models.EmailField(max_length=255,null=True)
        date=models.DateField()
        time=models.TimeField()