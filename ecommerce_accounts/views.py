from django.shortcuts import render, redirect
from .models import EcommerceUser
from .forms import EcommerceCustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import  auth
from django.core.mail import send_mail
import random
from ecommerce_accounts.email import email

# Create your views here.
def createaccount(request):
    return render(request, 'createaccount.html')
def create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        company_name = request.POST['company']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        country = request.POST['country']
        address= request.POST['address']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        comment = request.POST['comment']
        print('details: ',first_name, last_name, password1, password2, company_name, email, country, address, city, zipcode, comment)

        if EcommerceUser.objects.filter(email=email).exists():
            messages.info(request, 'Email already registered')
        else:
            if EcommerceUser.objects.filter(phone_number=phone_number):
                messages.info(request, 'Phone number already registered')
            else:
                if password1 == password2:
                    user = EcommerceUser.objects.create_user(first_name = first_name, last_name= last_name, password = password1, email= email,company_name = company_name, address= address,
                                           town= city, country = country, zipcode= zipcode, phone_number = phone_number,
                                           comment = comment)
                    user.save()
                    messages.success(request,'Your account created successfully')
                    return redirect('/accounts/login')
                else:
                    messages.info(request, 'Password not matching')

    return render(request, 'createaccount.html')
def loginpage(request):
    return render(request, 'login.html')
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email = email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def forgot_password(request):

    return render(request,'forgot_password.html')
def send_otp(request):
    email()
    otp = random.randint(0000,9999)
    '''send_mail(subject='OTP',
              message='OTP : %d'%otp,
              from_email='ravikiranb36@gmail.com',
              recipient_list=['ravikiranb36@yahoo.com'],
              fail_silently=False,
              )'''
    return render(request, 'forgot_password.html',{'otp_sent':True})