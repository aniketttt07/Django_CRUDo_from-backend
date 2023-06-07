from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):

 # Check if the request method is POST
    if request.method == 'POST':                
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        profile_image = request.FILES.get('image')

# Create Profile in database query 
        Profile.objects.create(
            name = name,
            email = email,
            mobile_number = mobile_number,
            address= address,
            profile_image=profile_image
        )
        return redirect('/')

# Retrieve all profile data from the database
    data = Profile.objects.all()

# Search funtionality query
    if request.GET.get('search'):
        data = data.filter(name__icontains = request.GET.get('search'))
        

    context = {
        'data' : data
    }

    return render(request, 'employeeForm.html',context)


def delete(request,id):
    query = Profile.objects.get(id=id)      # Retrieve the profile object with the id from the database
    query.delete()                          # Delete the retrive data from database
    return redirect('/')                    # Redirect to the home

def update(request,id):
    query = Profile.objects.get(id=id)

    if request.method == 'POST':
        # Retrived data form request
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        profile_image = request.FILES.get('image')

# Update the profile data with the retrieved data
        query.name = name
        query.email = email
        query.mobile_number = mobile_number
        query.address = address
        # Check if a new profile image was selected and update it accordingly
        if profile_image:
            query.profile_image = profile_image
        query.save()                                    # Save the updated data in database
        return redirect('/')                            # Redirect to the home

    context = {
        'query' : query
    }
    return render(request, 'updateForm.html',context)