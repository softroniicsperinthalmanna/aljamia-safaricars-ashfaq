from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import sell_your_car,feedback,address,service,test


class UserRegistrationForm(UserCreationForm):
    attrs = {
        "type": "password",
        'class':'form-control',
        'placeholder':'Enter your password ' 
    }  
    attrs1 = {
        "type": "password",
        'class':'form-control',
        'placeholder':'Confirm password ' 
    } 
    username = forms.CharField(max_length=101,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':'Enter User name'}))
    first_name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':'Enter your first name'}))
    last_name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':'Enter your last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':'Enter your email'}))
    password1 = forms.CharField(label='password',widget=forms.TextInput(attrs=attrs))
    password2 = forms.CharField(label='confirom',widget=forms.TextInput(attrs=attrs1))
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
      
       
    #    sell your car form

GEAR =(
        ('automatic transmisson','AUTOMATIC TRANSMISSION'),
        ('manual transmisson','MANUALTRANSMISSION')
)
FUEL= (
        ('petrol','PETROL'),
        ('deisel','DEISEL'),
        ('hybrid','HYBRID'),
        ('ev','ELECTRIC'),


)
class SellcarForm(forms.ModelForm):
     name = forms.CharField(max_length=25,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':' name'}))
     mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' mobile number'}))
     email = forms.EmailField(max_length=255,widget=forms.EmailInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' email '}))
     brand= forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':' brand'}))
     model= forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' model'}))
     year= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' year'}))
     km_driven= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' km driven '}))
     mailage= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' mailage'}))
     Color= forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':' color'}))
     no_owner= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' no_owner'}))
     engine_CC= forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':'Engine CC'}))
     insurence_validity= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':'  insurence_validity'}))
     year_of_registration= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' year_of_registration'}))
     transmisson= forms.ChoiceField(widget=forms.Select,choices=GEAR)
     fuel=forms.ChoiceField(widget=forms.Select,choices=FUEL)
     discription=forms.CharField(max_length=255,widget=forms.Textarea(attrs={'class':'form-control' ,'placeholder':'Enter any discription','rows':'5','style':'resize:none' }))
     image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control' , 'autocomplete': 'off'}))
     parking_sensor = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'width:50px;height:20px;','type':'checkbox'}))
     center_lock = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'width:50px;height:20px;','type':'checkbox' }))
     Rear_camera = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'width:50px;height:20px;','type':'checkbox' }))
     Navigation_system = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'width:50px;height:20px;','type':'checkbox' }))
     Adjustable_stearing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style':'width:50px;height:20px;','type':'checkbox'}))
     class Meta:
        model = sell_your_car
        fields = ['name','mobile','email','brand','model','year',
                  'km_driven','mailage','Color','no_owner','engine_CC',
                  'insurence_validity','year_of_registration','transmisson',
                  'fuel','discription','image','parking_sensor','Rear_camera',
                  'Navigation_system','Adjustable_stearing']
        labels = {"text": "", "public": "label for public"}

class fbForm(forms.ModelForm):
    name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':' your name'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' mobile number' }))
    email = forms.EmailField(max_length=255,widget=forms.EmailInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' Email','style':'paddind:10px' }))
    message = forms.CharField(max_length=255,widget=forms.Textarea(attrs={'class':'form-control' ,'placeholder':'Enter your feedback','rows':'5','style':'resize:none' }))
    class Meta:
       model = feedback
       fields=['name','mobile','email','message']

class addressForm(forms.ModelForm):
        name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':'  Name'}))
        mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'mobile number'}))
        email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'  Email'}))
        address =  forms.CharField(max_length=255,widget=forms.Textarea(attrs={'class':'form-control' ,'placeholder':'Enter your Address','rows':'5','style':'resize:none' }))
        city =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'  City'}))
        district =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'  District'}))
        pincode =  forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'  Pincode'}))
        class Meta:
            model =address
            fields =['name','mobile','email','address','city','district','pincode']
            
            
            

class testForm(forms.ModelForm):
    name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':' your name'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' mobile number' }))
    email = forms.EmailField(max_length=255,widget=forms.EmailInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' Email' }))
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' Date','type':'date' }))
    time=forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control', 'autocomplete': 'off','placeholder':' Time','type':'time' }))
    class Meta:
        model =test
        fields=['name','mobile','email','date','time']
        
        
class serviceForm(forms.ModelForm):
    delv =(
        ('pickup','PICKUP'),
        ('drop','DROP'),
        ('pick and drop','PICKUP AND DROP'),   
        ('not required','NOT REQUIRED')
)     
    servic =(
          ('water service','WATER SERVICE'),
          ('running repair','RUNNING REPAIR'),
          ('Accessories fitiing','ACCESSORIES FITTING'),
          ('Paint & polish','PAINT & POLISH'),
          ('Oil change','OIL CHANGE'),
          ('others','OTHERS')
) 
    name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only ','placeholder':' Name' }))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' mobile number' }))
    email = forms.EmailField(max_length=255,widget=forms.EmailInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' Email' }))
    car=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' Model' }))
    brand=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' brand' }))
    reg_no=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','placeholder':' reg_no' }))
    serv=forms.ChoiceField(widget=forms.Select,choices=servic)#dropdown
    deliv=forms.ChoiceField(widget=forms.Select,choices=delv)#dropdown
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control' ,'placeholder':' date','type':'date' }))
    class Meta:
       model =service
       fields=['name','mobile','email','car','brand','reg_no','serv','deliv','date']
     