from django.shortcuts import redirect, render
import random

def homepage(request):
    return render(request, 'homepage.html')


def result(request):
    if request.method == 'POST':
        characters = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '1234567890'
        special ='!@#$%&'
        upper ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
        if request.POST.get('numbers'):
            characters += numbers
        
        if request.POST.get('special'):
            characters += special

        if request.POST.get('upper'):
            characters += upper 

        length = int(request.POST.get('length'))

        password = ''
        
        for i in range(length):
            password += random.choice(characters)
    
        return render(request, 'result.html', {'password': password})
    else:
        return redirect('generator:homepage')

def about(request):
    return render(request, 'about.html')



    