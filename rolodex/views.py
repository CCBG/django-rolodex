from django.shortcuts import render

import os

import pprint as pp

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


import rolodex.models as Models
import rolodex.forms  as Forms

#@login_required(login_url='/login/')
def index(request):
    return render( request, "base.html")



# company related urls
@login_required(login_url='/login/')
def company_add( request ):

    if request.method == 'POST':
        company_form = Forms.CompanyForm( request.POST )

        if company_form.is_valid():

            # Save the company information the use submitted
            company = company_form.save()

            pp.pprint( company.id )

            return company_list( request )

        else:

            pp.pprint (company_form.errors)

            # The supplied form contained errors - re-render the page with the errors
            return render( request, 'rolodex/company_add.html', { 'company_form': company_form })
        
    else:
        company_form = Forms.CompanyForm()
        
        return render( request, "rolodex/company_add.html", {'company_form': company_form})


@login_required(login_url='/login/')
def company_edit( request, company_name ):

    company = Models.Company.objects.get( name__exact = company_name )

    if request.method == 'POST':

        company_form = Forms.CompanyForm(request.POST, instance=company)

        if company_form.is_valid():

            company = company_form.save()

            return HttpResponseRedirect(reverse( "company_list"))

        else:
            return render( request, 'rolodex/company_edit.html', { 'company_form': company_form})
        
    else:

        # Initialise the form with the data from the company model fetched above
        company_form = Forms.CompanyForm( instance = company )


        return render( request, 'rolodex/company_edit.html', { 'company_form': company_form })


def company_list( request ):
    companies = Models.Company.objects.all().order_by( 'name' )



    return render( request, 'rolodex/company_list.html', {'companies': companies});

@login_required(login_url='/login/')
def company_delete( request, company_name ):

    company = Models.Company.objects.get( name__exact = company_name )

    if ( request.method == 'POST' and 'company_delete' in request.POST ):

        company.delete()

        return( company_list( request ))

    else:

        company = Models.Company.objects.get( name__exact = company_name )
        
        return render(request, 'rolodex/company_delete.html', { 'company': company })



@login_required(login_url='/login/')
def contact_add( request, company_name = None ):
    if request.method == 'POST':
        contact_form = Forms.ContactForm( request.POST )

        if contact_form.is_valid():

            # Save the contact information the use submitted
            contact = contact_form.save()

            return contact_list( request, company_name )

        else:

            # The supplied form contained errors - re-render the page with the errors
            return render( request, 'rolodex/contact_add.html', { 'contact_form': contact_form })
        
    else:
        context = {'contact_form': Forms.ContactForm()}

        if company_name is not None:
            context['domain_name'] = domain_name

        
        return render( request, "rolodex/contact_add.html", context)

@login_required(login_url='/login/')
def contact_edit( request, contact_id ):
    contact = Models.Contact.objects.get( pk = contact_id )

    if request.method == 'POST':

        contact_form = Forms.ContactForm(request.POST, instance=contact )

        if contact_form.is_valid():

            contact = contact_form.save()

            return HttpResponseRedirect(reverse( "contact_list"))

        else:
            return render( request, 'rolodex/contact_edit.html', { 'contact_form': contact_form,
                                                                   'contact_id' : contact_id})
        
    else:

        contact_form = Forms.ContactForm( instance = contact )


        return render( request, 'rolodex/contact_edit.html', { 'contact_form': contact_form,
                                                               'contact_id' : contact_id })

def contact_list( request, company_name = None ):

    if ( company_name is not None ):
        
        contacts = Models.Contact.objects.filter( company__name__exact = company_name ).order_by( 'name' )

    else:

        contacts = Models.Contact.objects.all().order_by( 'name' )

    return render( request, 'rolodex/contact_list.html', {'contacts': contacts});


@login_required(login_url='/login/')
def contact_delete( request, contact_id ):

    contact = Models.Contact.objects.get( pk = contact_id )

    if ( request.method == 'POST' and 'contact_delete' in request.POST ):

        contact.delete()

        return( contact_list( request ))

    else:

#        company = contact.company
        
        print "Company: ", contact.company.name

        contact.name = "'{name}' @ '{company}'".format( name=contact.name, company=contact.company.name)
        
        return render(request, 'rolodex/contact_delete.html', { 'contact': contact })



def doc_notes( request ):
    return render( request, 'rolodex/doc_notes.html')


