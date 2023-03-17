from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from . models import SELL_CAR,Address,Service,Feedback,Test_drive
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

# from uni_form.helpers import FormHelper, Submit, Layout, Fieldset, helper
class LoginForm(AuthenticationForm):
     username=UsernameField(widget=forms.TextInput(attrs={'autofocus ': 'True','class' : 'form-control'}))
     password=forms.CharField( widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus ': 'True','class' : 'form-control'}))
    # your_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus ': 'True','class' : 'form-control'}))
    phone_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control', 'max_length':'10'}))
    # last_name = forms.CharField(max_length=101)

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password1=forms.CharField(label="Password" , widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2=forms.CharField(label="Confirm password" , widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['username','phone_number', 'email', 'password1', 'password2']


class SellVehicleForm(forms.ModelForm):
       Extra_CHOICES=(
               ('Parking sensor', 'Parking sensor'),
               ('Center lock', 'Center lock'),
               ('Rear camera', 'Rear camera'),
               ('Navigation system', 'Navigation system'),
               ('Adjustable seats', 'Adjustable seats'),
               ('Adjustable stearing', 'Adjustable stearing'),
        )
       extras = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                      choices=Extra_CHOICES)
    #    extras = forms.MultipleChoiceField(choices=Extra_CHOICES)
       class Meta:
       

        model=SELL_CAR
        fields = ['name','mobile','email','brand','model','year','km_driven','mileage','color','No_of_owners','engine_cc','Insurance_validity','year_of_registration','mode_of_transmission','type_of_vehicle','vehicle_description','vehicle_images','extras']
        widgets={
            'name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px; text-align:center;'}),
            'mobile':forms.NumberInput(attrs={'class' : 'form-control', 'style': 'width: 300px;text-align:center;'}),
            'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'brand':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'model':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'year':forms.NumberInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'km_driven':forms.NumberInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'milegae':forms.NumberInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'color':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'No_of_owners':forms.NumberInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'engine_cc':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'Insurance_validity':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'year_of_registration':forms.NumberInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'mode_of_transmission':forms.Select(attrs={'class' : 'form-control','style': 'width: 350px; text-align:center;'}),
            'type_of_vehicle':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            'vehicle_description':forms.Textarea(attrs={'class' : 'form-control','style': 'width: 500px; text-align:center;'}),
            'vehicle_images':forms.FileInput(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),
            # 'extras':forms.CheckboxSelectMultiple(attrs={'class' : 'form-control','style': 'width: 300px; text-align:center;'}),

        }    

class UserAddressForm(forms.ModelForm):
     class Meta:
        model=Address
        fields = ['name','phone_number', 'email', 'address', 'city','state','pincode']
        widgets={
            'name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
            'phone_number':forms.NumberInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
            'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'address':forms.Textarea(attrs={'class' : 'form-control','style': 'width: 400px;'}),
            'city':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'state':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'pincode':forms.NumberInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
        }



# class ServiceForm(forms.ModelForm):

#     #your details
#     name=forms.CharField()
#     phone_number= forms.CharField()
#     email=forms.EmailField()

#     #Vehicle details
#     car_model = forms.CharField()
#     brand = forms.CharField()
#     reg_no= forms.CharField()

#     #service details
#     type_of_service = forms.ChoiceField()
#     mode_of_vehicle_taking=forms.ChoiceField()
#     service_booked_for=forms.DateTimeField()

#     # now attach a uni_form helper to display the form
#     # helper = FormHelper()
    

#     # create the layout
#     layout = Layout(
#          # first fieldset
#          Fieldset("Your details",
#              'name', 'phone_number','email'),
#          Fieldset("Vehicle details",
#              'car_model', 'brand','reg_no'),
#          Fieldset("Service details",'type_of_service','mode_of_vehicle_taking','service_booked_for')
#     )     

#     # and add a submit button
#     submit = Submit('add', 'Submit information')
#     def __init__(self, *args, **kwargs):
#         self.helper = FormHelper()
#         self.helper.form_method = 'GET'
#         return super(ServiceForm, self).__init__(*args, **kwargs)
#     helper.add_input(submit)
class ServiceForm(forms.ModelForm):
     class Meta:
        model=Service
        fields = ['name','phone_number', 'email', 'car_model', 'brand','reg_no','type_of_service','mode_of_vehicle_taking','service_booked_on']
        widgets={
            'name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
            'phone_number':forms.NumberInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
            'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'car_model':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'brand':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'reg_no':forms.TextInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'type_of_service':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'mode_of_vehicle_taking':forms.Select(attrs={'class' : 'form-control','style': 'width: 300px;'}),
            'service_booked_on':forms.DateInput(attrs={'class' : 'form-control','type': 'date','style': 'width: 300px;'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
       model=Feedback   
       fields=['name','phone_number','message']
       widgets={
          'name':forms.TextInput(attrs={'class' : 'form-control,text-center', 'style': 'width: 300px;'}),
          'phone_number':forms.NumberInput(attrs={'class' : 'form-control,text-center', 'style': 'width: 300px;'}),
          'message':forms.Textarea(attrs={'class' : 'form-control,text-center','style': 'width: 300px;'}),

       }  

class TestdriveForm(forms.ModelForm):
    class Meta:
       model=Test_drive   
       fields=['name','phone_number','email','vehicle_name','select_date','select_time']
       widgets={
          'name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
          'phone_number':forms.NumberInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
          'email':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
          'vehicle_name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
          'select_date':forms.DateInput(attrs={'class' : 'form-control','type': 'date','style': 'width: 200px;'}),
          'select_time':forms.TimeInput(attrs={'class' : 'form-control','type': 'time','style': 'width: 200px;'}),

       } 


# class OrderForm(forms.ModelForm):
#         class Meta:
#           model=Test_drive   
#           fields=['Your_name','Product','contact_number','Contact_info','Quantity']
#           widgets={
#           'Your_name':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
#           'Product':forms.NumberInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
#           'contact_number':forms.EmailInput(attrs={'class' : 'form-control','style': 'width: 300px;'}),
#           'Contact_info':forms.TextInput(attrs={'class' : 'form-control', 'style': 'width: 300px;'}),
#           'Quantity':forms.NumberInput(attrs={'class' : 'form-control','style': 'width: 200px;'}),
#            }    

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())