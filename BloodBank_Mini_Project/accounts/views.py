from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.http.response import JsonResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        name = request.POST['first_name']
        username= request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Alredy Exist!!!")
                return redirect("accounts:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Alredy Exist!!!")
                return redirect("accounts:register")
            else:
                user = User.objects.create_user(username=username, email=email,password=password, first_name=name)
                user.save()
                print('user created')
                return redirect("accounts:login")
        else:
            messages.info(request," password is not match!!!")
            return redirect("accounts:register")
        return redirect("accounts:login")
    else:   
        return render(request,"register.html")

def user_login(request):
    if 'username' in request.session:
        return redirect("BloodBank_app:result")
    elif request.method== 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['username']=username
            auth.login(request,user)
            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            auth.login
            return JsonResponse(
                {'success':False},
                safe=False
            )
        #     return redirect('BloodBank_app:result')
        # else:
        #     auth.login
        #     messages.info(request,"Invalid Details!!!")
        #     return redirect('accounts:login')
    else:
        return render(request,"login.html")





def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('accounts:login')    