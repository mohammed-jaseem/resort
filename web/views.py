from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from web.models import *


@login_required(login_url='/login')
def index(request):
    rooms = Room.objects.all()[:3]
    context = {
        'rooms': rooms
    }
  
    return render(request, 'web/index.html', context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password,) 

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error':True,
                'message':'Invalid email or password'
            }
            return render(request, 'web/login.html', context=context)
    else:
        return render(request, 'web/login.html')
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password,
        )
        user.save()
        return HttpResponseRedirect(reverse('web:login'))
    
    else:
        return render(request, 'web/register.html')
    
@login_required(login_url='/login')    
def logout(request):
    user = request.user
    auth_logout(request)

    return HttpResponseRedirect(reverse('web:login'))

def booking(request):

    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }

    return render(request, 'web/booking.html', context=context)

def reviews(request):
    rewiew = Rewiew.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        short_discription = request.POST.get('short_discription')
        rating = request.POST.get('rating')

        rewiew = Rewiew.objects.create(
            name=name,
            short_discription=short_discription,
            rating=rating,
            )
        rewiew.save()
        return HttpResponseRedirect(reverse('web:reviews'))
    
    context ={
        'rewiew':rewiew,        
    }

    return render(request, 'web/reviews.html', context=context)

def amenities(request):
    return render(request, 'web/amenities.html',)

def contact(request):
    return render(request, 'web/contact.html',)

def rooms(request,id):
    user = request.user
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        rooms_type = request.POST.get('rooms_type')
        check_date = request.POST.get('check_date')
        checkout_date = request.POST.get('checkout_date')
        number = request.POST.get('number')
        request_guests = request.POST.get('request_guests')


        detail = Detail.objects.create(
            user=user,
            room=room,
            fullname=fullname,
            email=email,
            rooms_type=rooms_type,
            check_date=check_date,
            checkout_date=checkout_date,
            number=number,
            request_guests=request_guests,
            )
        detail.save()
        return HttpResponseRedirect(reverse('web:boock-recived'))
    
    return render(request, 'web/rooms.html')


def boock_recived(request):
    user = request.user
    details = Detail.objects.filter(user=user)

    context = {
        'details': details
    }

    return render(request, 'web/boock-recived.html', context=context)


