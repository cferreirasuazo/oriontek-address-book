from django import forms

from core.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address1',
                  'address2',
                  'city',
                  'phone_number',
                  'country_province',
                  'zip_code',
                  'country',
                  'details' ]
