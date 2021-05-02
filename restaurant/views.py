from django.shortcuts import render
from . import models

def home(request):
    return render(request,'form.html')

def ins_upd_del(request):
    if request.method == 'POST':
        if request.POST["action"]=="Insert":
            obj=models.food()
        elif request.POST["action"]=="Update":
            nameid=request.POST["food"]
            obj=models.food.objects.get(name=nameid)
        elif request.POST["action"]=="Delete":
            nameid=request.POST["food"]
            obj=models.food.objects.get(name=nameid)
            obj.delete()
            return render(request,'form.html')
        obj.name=request.POST["food"]
        obj.price=request.POST["price"]
        obj.des=request.POST["discp"]
        obj.cuisine=request.POST["cuisine"]
        try:
                obj.chk1=request.POST["chk1"]
        except:
                obj.chk1=False
       
        try:
                obj.chk3=request.POST["chk3"]
        except:
                obj.chk3=False
        obj.dat=request.POST["date"]
        obj.radio=request.POST["rd"]
        obj.img=request.FILES["img"]
        obj.save()
    return render(request,'form.html')

def disp(request):
    obj=models.food.objects.all()
    return render(request,'menu.html',{"all_obj":obj})

    