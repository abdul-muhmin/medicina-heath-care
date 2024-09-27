from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib.auth import login,authenticate,logout
from  django.contrib import messages
# Create your views here.
def signout(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True

        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #create user acounts
            user=User.objects.create_user(
                
                username=username,
                password=password,
                email=email
            )
            #create customer account
            customer=Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            success_message="user registred successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Duplicate username or invalid data inputs"
            messages.error(request,error_message)
            
    if request.POST and 'login' in request.POST:
        
        context['register']=False
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'invalid user credentails.')
        

    return render(request,'account.html',context)