from django import forms
from ecommerce_accounts.models import EcommerceUser
class EcommerceCustomerForm(forms.ModelForm):
    password1 = forms.CharField(  widget=forms.PasswordInput(), label='Enter password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Re-enter password')
    class Meta:
        model = EcommerceUser
        fields = ('first_name', 'email', 'last_name',  'password1', 'password2', 'company_name', 'country',
                  'address', 'town', 'zipcode', 'comment')