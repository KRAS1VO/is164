from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    total_count = 555
    return render(request, 'home.html', {'total_count': total_count})

def today(request):
    return HttpResponse('Hi bro this is Today page')

def password(request):
    caracters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('number'):
        caracters.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        caracters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        caracters.extend(list('!@#$%^&*()_=+?'))
    lenght = int(request.GET.get('lenght',10))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(caracters)
    context ={'thepassword': thepassword}

    return render(request, 'password.html', {'thepassword': thepassword})

def about(request):
    return render(request, 'about.html')