from django import forms
from  .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import UserProfile
from datetime import date

YEARS= [x for x in range(1940,2021)]

class UserRegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Must be at least 18 years old to register')
        return dob
    class Meta:
        model  = CustomUser
        fields = [ 'email' , 'password1' , 'password2', 'date_of_birth']


class UserProfileForm(ModelForm):

    class Meta:
        model  = UserProfile
        exclude = ['user' , 'matches' , 'pending', 'interests']