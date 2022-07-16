from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'soldierLetter/base.html')

def login(request):
    return render(request, 'soldierLetter/base.html')