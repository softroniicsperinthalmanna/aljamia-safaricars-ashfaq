from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import sell_your_car,feedback,address,service,test


class UserRegistrationForm(UserCreationForm):
    attrs = {
        "type": "password"
    }  
    username = forms.CharField(max_length=101,label='User name')
    first_name = forms.CharField(max_length=101,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    last_name = forms.CharField(max_length=101,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    email = forms.EmailField()
    password1 = forms.CharField(label='password',widget=forms.TextInput(attrs=attrs))
    password2 = forms.CharField(label='confirom',widget=forms.TextInput(attrs=attrs))
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
      
       
    #    sell your car form

class SellcarForm(forms.ModelForm):
     name = forms.CharField(max_length=25,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
     mobile = forms.IntegerField()
     email = forms.EmailField(max_length=255)
     brand= forms.CharField(max_length=255)
     model= forms.CharField(max_length=255)
     year= forms.CharField(max_length=255)
     km_driven= forms.CharField(max_length=255)
     mailage= forms.CharField(max_length=255)
     Color= forms.CharField(max_length=255)
     no_owner= forms.CharField(max_length=255)
     engine_CC= forms.CharField(max_length=255)
     insurence_validity= forms.CharField(max_length=255)
     year_of_registration= forms.CharField(max_length=255)
     transmisson= forms.CharField(max_length=255,)
     fuel=forms.ChoiceField()#dropdown
     discription=forms.CharField(max_length=255)
     image = forms.ImageField()
     parking_sensor = forms.BooleanField()
     center_lock = forms.BooleanField()
     Rear_camera = forms.BooleanField()
     Navigation_system = forms.BooleanField()
     Adjustable_stearing = forms.BooleanField()
     class Meta:
        model = sell_your_car
        fields = ['name','mobile','email','brand','model','year',
                  'km_driven','mailage','Color','no_owner','engine_CC',
                  'insurence_validity','year_of_registration','transmisson',
                  'fuel','discription','image','parking_sensor','Rear_camera',
                  'Navigation_system','Adjustable_stearing']
        labels = {"text": "", "public": "label for public"}

class fbForm(forms.ModelForm):
     name = forms.CharField(max_length=255 ,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
     mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
     email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
     message = forms.CharField(max_length=255,widget=forms.Textarea(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
     class Meta:
       model = feedback
       fields=['name','mobile','email','message']

class addressForm(forms.ModelForm):
        name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
        mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
        address =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
        city =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
        district =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
        pincode =  forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
        class Meta:
            model =address
            fields =['name','mobile','email','address','city','district','pincode']
            
            
            

class testForm(forms.ModelForm):
    name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    mobile = forms.IntegerField()
    email = forms.EmailField(max_length=255)
    date=forms.DateField()
    time=forms.TimeField()
    class Meta:
        model =test
        fields=['name','mobile','email','date','time']
        
        
class serviceForm(forms.ModelForm):
    name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}))
    mobile = forms.IntegerField()
    email = forms.EmailField(max_length=255)
    car=forms.CharField(max_length=255)
    brand=forms.CharField(max_length=255)
    reg_no=forms.CharField()
    serv=forms.CharField(max_length=255)#dropdown
    deliv=forms.CharField(max_length=255)#dropdown
    date=forms.DateField()
    class Meta:
       model =service
       fields=['name','mobile','email','car','brand','reg_no','serv','deliv','date']