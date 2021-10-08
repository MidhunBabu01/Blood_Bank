from django.shortcuts import redirect, render
from django.http.response import HttpResponse

# Create your views here.
# loginn =[]
def index(request):
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # login = {
    #     'email':email,
    #     'password':password,
    # }
    # if reg == login:
    #     reg.save()
    return render(request,"index.html")
 
 
 
context = []
def result(request):
    name = request.POST.get('name')
    phone = request.POST.get('number')
    age = request.POST.get('age')
    blood_grp = request.POST.get('group')
    datas ={
        'name':name,
        'phone':phone,
        'age':age,
        'blood_grp':blood_grp,
    }
    context.append(datas)
    return render(request,"result.html",{'datas':context})


# def register(request):
#     return render(request,"register.html")

# reg = []
# def login(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     phone = request.POST.get('phone')
#     password = request.POST.get('password')
#     password2 = request.POST.get('password2')
#     context = {
#         'name':name,
#         'email':email,
#         'phone':phone,
#         'password':password,
#         'password2':password2
#     }
#     reg.append(context)
#     return render(request,"login.html",{'user':reg})