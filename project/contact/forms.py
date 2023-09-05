from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Write some stuff'
            }
        ),
        label='First NAME',
        help_text='Write something pal',
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
    )
    )
    

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description','category','picture',)

    def clean(self):

        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        

        if first_name == last_name:
            error_msg = ValidationError('Primeiro nome não pode ser igual ao sobrenome',code='invalid')
            self.add_error('first_name', error_msg)
            self.add_error('last_name', error_msg)
            
        return super().clean()
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        )
    last_name = forms.CharField(
        required=True, 
        min_length=3,
        )
    email = forms.EmailField()

    class Meta():
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
            )
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email já existe', code='invalid')
                
            )