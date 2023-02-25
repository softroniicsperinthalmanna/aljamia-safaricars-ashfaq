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
class add_vehicle(models.Model):
   
     
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
     image1 = models.ImageField( max_length = 100,null=True)
     image2 = models.ImageField( max_length = 100,null=True)
     image3 = models.ImageField( max_length = 100,null=True)
     image4 = models.ImageField( max_length = 100,null=True)

     parking_sensor = models.BooleanField( "parking_sensor",default=False)
     center_lock = models.BooleanField( "center_lock",default=False)
     Rear_camera = models.BooleanField( "Rear_camera",default=False)
     Navigation_system = models.BooleanField( "Navigation_system",default=False)
     Adjustable_stearing = models.BooleanField( "Adjustable_stearing",default=False)
     c_price= models.IntegerField(null=True)

class add_product(models.Model):
        p_name=models.CharField(max_length=255)
        p_price=models.IntegerField()
        discription=models.CharField(max_length=255)
        image = models.ImageField( max_length = 100)

class dis_product(models.Model):
        p_name=models.CharField(max_length=255)
        p_price=models.IntegerField()
        discription=models.CharField(max_length=255)
        image = models.ImageField( max_length = 100)

        
class l_cars(models.Model):
     l_brand= models.CharField(max_length=255)
     l_model= models.CharField(max_length=255)
     l_year= models.IntegerField()
     l_km_driven= models.IntegerField()
     l_Color= models.CharField(max_length=255)
     l_no_owner= models.IntegerField()
     l_engine_CC= models.CharField(max_length=255)
     l_insurence_validity= models.IntegerField()
     l_transmisson= models.CharField(max_length=255, choices=GEAR, default='manual')
     l_fuel=models.CharField(max_length=255,choices=FUEL, default='petrol')
     l_discription=models.CharField(max_length=255)
     l_image = models.ImageField( max_length = 100)
     l_price =models.IntegerField()

class l_bikes(models.Model):
     b_brand= models.CharField(max_length=255)
     b_model= models.CharField(max_length=255)
     b_year= models.IntegerField()
     b_km_driven= models.IntegerField()
     b_Color= models.CharField(max_length=255)
     b_no_owner= models.IntegerField()
     b_engine_CC= models.CharField(max_length=255)
     b_insurence_validity= models.IntegerField()
     b_transmisson= models.CharField(max_length=255, choices=GEAR, default='manual')
     b_fuel=models.CharField(max_length=255,choices=FUEL, default='petrol')
     b_discription=models.CharField(max_length=255)
     b_image = models.ImageField( max_length = 100) 
     b_price =models.IntegerField()

class add_garage(models.Model):
        place = models.CharField(max_length=255)
        mobile = models.IntegerField()
        g_image = models.ImageField( max_length = 100) 
        g_discription=models.CharField(max_length=255)

class add_featre_ad(models.Model):
        f_image = models.ImageField( max_length = 100) 
