

from django.shortcuts import render

def uzbek(request):
    return render(request, 'uz.html')

def rus(request):
    return render(request, 'rus.html')

def englw(request):
    return render(request, 'englw.html')

# Create your views here.
