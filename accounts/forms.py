from django.contrib.auth.models import User
from django.forms import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
