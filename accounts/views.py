from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth 
from django.shortcuts import redirect
from django.http import JsonResponse

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password1'])
            user.is_active = False
            user.save()
            
            auth.login(request, user)
            return redirect('/intro')

    return render(request, 'accounts/signup.html')

def subscribe(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.profile.name = request.POST['name']
        user.profile.birthday = request.POST['birthday']
        user.profile.army_type = request.POST['army_type']
        user.profile.unit_type = request.POST['unit_type']
        user.profile.enter_date = request.POST['enter_date']
        user.profile.sub_type1 = request.POST['sub_type1']
        user.profile.sub_type2 = request.POST['sub_type2']
        if (request.POST.get('stock_type', False) != False):
            user.profile.stock_type = request.POST['stock_type']
        user.profile.subscribe = True
        user.save()
        return redirect('/intro')

    return render(request, 'accounts/subscribe.html')

def edit(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.profile.name = request.POST['name']
        user.profile.birthday = request.POST['birthday']
        user.profile.army_type = request.POST['army_type']
        user.profile.unit_type = request.POST['unit_type']
        user.profile.enter_date = request.POST['enter_date']
        user.profile.sub_type1 = request.POST['sub_type1']
        user.profile.sub_type2 = request.POST['sub_type2']
        user.profile.subscribe = True
        user.save()
        return redirect('/intro')
    
    user = User.objects.get(id=request.user.id)
    name = user.profile.name
    birthday = user.profile.birthday
    army_type = user.profile.army_type
    unit_type = user.profile.unit_type
    enter_date = user.profile.enter_date
    sub_type1 = user.profile.sub_type1
    sub_type2 = user.profile.sub_type2

    return render(request, 'accounts/edit.html', {'name':name, 'birthday':birthday, 'army_type':army_type, 'unit_type':unit_type, 'enter_date':enter_date, 'sub_type1':sub_type1, 'sub_type2':sub_type2})

def check(request):
    username = request.POST['content']
    print('아이디 중복 체크')
    try:
        user = User.objects.get(username=username)
    except:
        user = None
    if user is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    return JsonResponse({'duplicate': duplicate})