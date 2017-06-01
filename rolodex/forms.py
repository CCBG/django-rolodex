from django import forms
from django.forms import ModelForm

import rolodex.models as Models

import re
import pprint as pp

class CompanyForm( ModelForm ):
    """
    Form for adding a new company to the database. 

    """
    
    class Meta:
        model = Models.Company
        fields = ['name',]#'__all__'


class ContactForm( ModelForm ):
    """
    Form for adding new domains to the database. 

    """
    company       = forms.ModelChoiceField(queryset=Models.Company.objects.all().order_by('name'), label="Select company")
    
    class Meta:
        model = Models.Contact
        fields = ['name','company', 'note']

