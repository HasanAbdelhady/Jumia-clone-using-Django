from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _ , field in self.fields.items():
            field.widget.attrs.update({
                'class': 'm-4 w-1/2 px-4 py-2 border border-gray-300 rounded-lg'
            })
    usable_password = None

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

