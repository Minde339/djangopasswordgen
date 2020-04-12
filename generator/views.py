from django.shortcuts import render
import random

def home(request,*args,**kwargs):
    return render(request,'generator/home.html')
def about(request,*args,**kwargs):
    return render(request, 'generator/about.html')
def password(request,*args,**kwargs):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length',12))

    thepass = ''
    for x in range(length):
        thepass += random.choice(characters)

    return render(request,'generator/password.html', {'password':thepass})

# Create your views here.
