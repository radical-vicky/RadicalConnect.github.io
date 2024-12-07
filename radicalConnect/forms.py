from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from radicalConnect.models import Contact, FutureSkill
from django.contrib.auth.models import User



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


        widgets = {
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control', 'accept': 'images/*', 'title': 'Upload your image here'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Full Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email'}),
            'phoneNumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your Phone Number','value':'+254'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}),
            'age': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your Age'}),
            'county': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your County'}),
            'subject': forms.Select(attrs={'class':'form-control', 'placeholder':'What do you want'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Occupation (optional)'}),

        }





class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def __str__(self):
        return f"{self.cleaned_data['username']} ({self.cleaned_data['password']})"

    def save(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        return user






from django import forms

from django.contrib.auth.forms import UserCreationForm

class AccountForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields =['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
          }


class FutureSkillForm(forms.ModelForm):
    class Meta:
        model = FutureSkill
        fields = ['selected_skills']
        widgets = {
            'selected_skills': forms.Select(choices=FutureSkill.SKILL_CHOICES)
        }
