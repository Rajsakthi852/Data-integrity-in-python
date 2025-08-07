from django.shortcuts import render, HttpResponse, redirect
from.models import register

# Create your views here.
def registerpage(request):
    if request.method == "POST":
        getname = request.POST["name"]
        getaddress = request.POST["address"]
        getusername = request.POST["username"]
        getpassword = request.POST["password"]
        users = register()
        users.Name = getname
        users.Address = getaddress
        users.Username = getusername
        users.Password = getpassword
        users.save()
    return render(request,"registerpage.html")

def userlog(request):
    if request.method == "POST":
        getusername = request.POST["username"]
        getpassword = request.POST["password"]
        try:
            register.objects.get(Username=getusername,Password=getpassword)
            return HttpResponse("Welcome User")
        except:
            return HttpResponse("Invalid User")
    return render(request,"userlogin.html")

def adminlog(request):
    if request.method == "POST":
        getusername = request.POST["username"]
        getpassword = request.POST["password"]
        if getusername == "admin" and getpassword == "admin":
            return redirect("/adminhome")
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,"adminlogin.html")

def adminhome(request):
    return render(request,"adminhome.html")

def pending(request):
    details = register.objects.filter(Status=False)
    return render(request,"pendinglist.html",{"value":details})

def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect("/pending")

def approved(request):
    details = register.objects.filter(Status=True)
    return render(request,"approvedlist.html",{"value":details})

def edit(request,id):
    details = register.objects.filter(Status=True)
    data = register.objects.get(id=id)
    if request.method == "POST":
        getaddress = request.POST["address"]
        getpassword = request.POST["password"]
        data.Address = getaddress
        data.Password = getpassword
        data.save()
        return redirect("/approved")
    return render(request, "approvedlist.html", {"value": details, "userdata": data})

def delete(request,id):
    data = register.objects.get(id=id).delete()
    return redirect("/approved")