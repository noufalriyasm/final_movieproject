from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def your_profile(request):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        user=request.user
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.save()
        messages.success(request,"Credentials Saved Succesfully")
        return redirect(url)
    return render(request,"profile.html",{'user':request.user})