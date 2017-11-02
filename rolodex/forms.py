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

    def clean_name(self):
        name =  self.cleaned_data['name']

        prev_instance = Models.Company.objects.filter( name__exact = name)
        pp.pprint( prev_instance )
        if ( len(prev_instance) ):
            raise forms.ValidationError("Not a unique company name!" )

        return name


class ContactForm( ModelForm ):
    """
    Form for adding new domains to the database. 

    """
    company       = forms.ModelChoiceField(queryset=Models.Company.objects.all().order_by('name'), label="Select company")
    
    class Meta:
        model = Models.Contact
        fields = ['name','company', 'note']


    def clean_name(self):
        cleaned_data = self.cleaned_data

        name =  cleaned_data['name']

        prev_instance = Models.Contact.objects.filter( name__exact = name)
        if ( len(prev_instance) ):
            raise forms.ValidationError("Not a unique contact name, {name} is currently working for {company}".format(name= name, company=prev_instance.company.name ))

        return name
