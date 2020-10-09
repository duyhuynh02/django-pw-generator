from django.shortcuts import render
from random import choice


def home(request):
    return render(request, 'home.html')

def generator(request):
    characters= list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    length = int(request.GET.get('length'), 12)
    mypassword = ''
    for c in range(length):
        generator_password = choice(characters)
        mypassword += generator_password
        
    return render(request,  'generator.html', {'password': mypassword})