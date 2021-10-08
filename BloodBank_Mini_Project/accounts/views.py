from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
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




def login(request):
    if request.method== 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('BloodBank_app:result')
        else:
            messages.info(request,"Invalid Details!!!")
            return redirect("accounts:login")
    else:
        return render(request,"login.html")



def logout(request):
    auth.logout(request)
    return redirect('/')