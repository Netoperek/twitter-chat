from django import forms
from webAppUser.models import WebAppUser

class WebAppUserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = WebAppUser
