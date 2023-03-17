from django.db import models
# from django.urls import reverse
# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
# from django.db.models.signals import post_save
User=get_user_model()

Transmission_CHOICES=(
    ('Manual', 'Manual Transmission'),
    ('Automatic', 'Automatic Transmission'),
)

Engine_CHOICES=(
    ('Diesel', 'Diesel'),
    ('Petrol', 'Petrol'),
    ('Electric', 'Electric'),
    ('Hybrid', 'Hybrid'),
)

STATE_CHOICES=(
    ('Chandigarh', 'Chandigarh'),
    ('Delhi', 'Delhi'), 
    ('Goa' , 'Goa'), 
    ('Jammu Kashmir', 'Jammu Kashmir'),
    ('Nagaland', 'Nagaland'),
    ('Rajasthan', 'Rajasthan'), 
    ('Uttarakhand', 'Uttarakhand'), 
    ('West Bengal', 'West Bengal'), 
    ('Ladakh','Ladakh'),
    ('Jharkhand','Jharkhand') ,
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Bihar', 'Bihar'),
    ('Tripura', 'Tripura'), 
    ('Telangana', 'Telangana'), 
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Punjab','Punjab'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Andhra Pradesh' , 'Andhra Pradesh'), 
    ('Meghalaya' , 'Meghalaya'), 
    ('Manipur', 'Manipur'), 
    ('Tamil Nadu', 'Tamil Nadu'), 
    ('Kerala' , 'Kerala' ),
    ('Haryana' , 'Haryana'),
    ('Gujarat' , 'Gujarat'), 
    ('Karnataka', 'Karnataka'), 
    ('Assam', 'Assam'),
)
Service_choices=(
    ('Running Repair', 'Running Repair'), 
    ('Water service' , 'Water service' ),
    ('Accessories fitting' , 'Accessories fitting'),
    ('Paint & polish' , 'Paint & polish'), 
    ('Oil change', 'Oil change'), 
    ('Other', 'Other'),
)
Pickup_choices=(
    ('Pickup & Drop', 'Pickup & Drop'), 
    ('Pickup only' , 'Pickup only' ),
    ('Drop only' , 'Drop only'),
    ('Not required' , 'Not required'), 
)




class SELL_CAR(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    mobile=models.IntegerField(default=0)
    email=models.EmailField()
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField()
    km_driven=models.IntegerField()
    mileage=models.IntegerField()
    color=models.CharField(max_length=100)
    No_of_owners=models.IntegerField()
    engine_cc=models.CharField(max_length=50)
    Insurance_validity=models.CharField(max_length=50)
    year_of_registration=models.IntegerField()
    mode_of_transmission=models.CharField(choices=Transmission_CHOICES, max_length=100)
    type_of_vehicle=models.CharField(choices=Engine_CHOICES, max_length=100)
    vehicle_description=models.TextField(help_text = "You can write more about your vehicle here")
    vehicle_images=models.ImageField(upload_to='images/')
    extras=models.CharField( max_length=100)

    # state=models.CharField(choices=STATE_CHOICES,max_length=100) 
    def __str__(self):
        return self.name

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField(default=0)
    email=models.EmailField()
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    pincode=models.IntegerField()

    def __str__(self):
        return self.name

class Service(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField(default=0)
    email=models.EmailField()
    car_model=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    reg_no=models.CharField(max_length=100)
    type_of_service=models.CharField(choices=Service_choices,max_length=150)
    mode_of_vehicle_taking=models.CharField(choices=Pickup_choices,max_length=100)
    service_booked_on=models.DateField()

class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    message=models.TextField()

   


class Test_drive(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    email=models.EmailField()
    vehicle_name=models.CharField(max_length=100)
    select_date=models.DateField()
    select_time=models.TimeField()

    
# class Transaction(models.Model):
#     made_by = models.ForeignKey(User, related_name='transactions', 
#                                 on_delete=models.CASCADE)
#     made_on = models.DateTimeField(auto_now_add=True)
#     amount = models.IntegerField()
#     order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
#     checksum = models.CharField(max_length=100, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if self.order_id is None and self.made_on and self.id:
#             self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
#         return super().save(*args, **kwargs)
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
   
     user=models.ForeignKey(User,on_delete=models.CASCADE)
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
     c_price= models.IntegerField(null=True)

# CATEGORY_CHOICES=(
#     ('LC', 'Laxury car'),
#     ('LB', 'Laxury Bikes'),
#     ('EV', 'Electric Vehicle'),
#     ('HV', 'Hybrid Vehicle'),    
# )
class add_product(models.Model):
        # prod_id = models.AutoField(primary_key=True, default=1)
        # user=models.ForeignKey(User,on_delete=models.CASCADE)
        p_name=models.CharField(max_length=255)
        p_price=models.IntegerField()
        discription=models.CharField(max_length=255)
        # category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
        image = models.ImageField( max_length = 100)

        def __str__(self):
             return self.p_name
        
class l_cars(models.Model):
    #  user=models.ForeignKey(User,on_delete=models.CASCADE)
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
    #  user=models.ForeignKey(User,on_delete=models.CASCADE)
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
        # user=models.ForeignKey(User,on_delete=models.CASCADE)
        place = models.CharField(max_length=255)
        mobile = models.IntegerField()
        g_image = models.ImageField( max_length = 100) 
        g_discription=models.CharField(max_length=255)

class add_featre_ad(models.Model):
        #  user=models.ForeignKey(User,on_delete=models.CASCADE)
         f_image = models.ImageField()

# class Profile(models.Model):
#     # user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     ebooks=models.ManyToManyField(add_product, on_delete=models.SET_NULL,null=True)
   
#     def __str__(self):
#         return self.user.username
# def post_save_profile_create(sender, instance, created, *args, **kwargs):
#     user_profile, created = Profile.objects.get_or_create(user=instance)

    # if user_profile.stripe_id is None or user_profile.stripe_id == '':
    #     new_stripe_id = stripe.Customer.create(email=instance.email)
    #     user_profile.stripe_id = new_stripe_id['id']
    #     user_profile.save()


# post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)        

# class OrderItems(models.Model):
#     product=models.OneToOneField(add_product, on_delete=models.SET_NULL,null=True)
#     is_ordered=models.BooleanField(default=False)
#     date_added=models.DateTimeField(auto_now=True)
#     date_ordered=models.DateTimeField(null=True)

#     def __str__(self):
#         return self.product.p_name


# class Order(models.Model):
#        owner=models.ForeignKey(User,on_delete=models.CASCADE) 
#        is_ordered=models.BooleanField(default=False)
#        items=models.ManyToManyField(OrderItems)
#        date_ordered=models.DateTimeField(auto_now=True)

#        def get_cart_items(self):
#            return self.items.all()

#        def get_cart_total(self):
#           return sum([item.product.p_price for item in self.items.all()])

#        def __str__(self):
#          return '{0} - {1}'.format(self.owner, self.ref_code)
 
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(add_product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.p_price

STATUS_CHOICES=(
     ('Accepted','Accepted'),
     ('Packed','Packed'),
     ('On The Way','On The Way'),
     ('Delivered','Delivered'),
     ('Cancel','Cancel'),
     ('Pending','Pending') 
)


class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    amount=models.FloatField()
    razorpay_order_id= models.CharField(max_length=100, blank=True, null=True) 
    razorpay_payment_status= models.CharField(max_length=100, blank=True, null=True) 
    razorpay_payment_id=models.CharField(max_length=100, blank=True, null=True)
    paid=models.BooleanField(default=False)
    





class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Address,on_delete=models.CASCADE)
    product=models.ForeignKey(add_product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES, default='pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")

    @property
    def total_cost(self):
         return self.quantity * self.product.p_price
