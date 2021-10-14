from django.shortcuts import redirect, render
from BloodBank_app.models import DonarDetails


def index(request):
    return render(request,"index.html")
 
 
 
# context = []
def result(request):
    if 'username' in request.session:
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('number')
            age = request.POST.get('age')
            blood_grp = request.POST.get('group')
            datas = DonarDetails.objects.create(name=name,age=age,phone=phone,blood=blood_grp)
            datas.save()
        result = DonarDetails.objects.all()
        return render(request,"result.html",{'datas':result})
    else:
        return redirect('accounts:login')
    
