from django.shortcuts import render,redirect
from StellarApp.models import admindb,categorydb,addproductdb,messagedb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User




# Create your views here.
def indexpg(request):
    return render(request,'index.html')
def adminpg(request):
    return render(request,'addadmin.html')
def admindb_fun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mob=request.POST.get('mob')
        email=request.POST.get('email')
        un=request.POST.get('username')
        psd=request.POST.get('pwd')
        cpsd=request.POST.get('cpwd')
        img=request.FILES['image']

        obj=admindb(Name=na,Mobile=mob,Email=email,Username=un,Password=psd,Conformpassword=cpsd,Image=img)
        obj.save()
    return redirect(adminpg)
def displayadminpg(request):
    data=admindb.objects.all()
    return render(request,'displayadmin.html',{'data':data})
def editadmin(request,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(request,'edit.html',{'data':data})
def updateadmin(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        un = request.POST.get('username')
        psd = request.POST.get('pwd')
        cpsd = request.POST.get('cpwd')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image

    admindb.objects.filter(id=dataid).update(Name=na,Mobile=mob,Email=email,Username=un,Password=psd,Conformpassword=cpsd,Image=file)
    return redirect(displayadminpg)
def deleteadmin(request,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadminpg)

def categorypg(request):
    return render(request,'addcategory.html')
def categorydb_fun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ds=request.POST.get('dis')
        img=request.FILES['image']
        obj=categorydb(Name=na,Discription=ds,Image=img)
        obj.save()
        return redirect(categorypg)
def displaycategorypd(request):
    data=categorydb.objects.all()
    return render(request,'displaycategory.html',{'data':data})
def editcategory(request,dataid):
    data=categorydb.objects.get(id=dataid)
    print(data)
    return render(request,'editcategory.html',{'data':data})
def updatecategory(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('dis')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image

    categorydb.objects.filter(id=dataid).update(Name=na,Discription=ds,Image=file)
    return redirect(displaycategorypd)
def deletecategory(request,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategorypd)


def addproductspg(request):
    data=categorydb.objects.all()
    return render(request,'addproduct.html',{'data':data})
def addproductdb_fun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        pr=request.POST.get('price')
        qt=request.POST.get('quantity')
        ds=request.POST.get('discription')
        ct=request.POST.get('category')
        img=request.FILES['image']
        obj=addproductdb(Name=na,Price=pr,Quantity=qt,Discription=ds,Category=ct,Image=img)
        obj.save()
        return redirect(addproductspg)
def displayproduct(request):
    data=addproductdb.objects.all()
    return render(request,'displayproduct.html',{'data':data})
def editproduct(request,dataid):
    data=addproductdb.objects.get(id=dataid)
    da=categorydb.objects.all()
    return render(request,'editproduct.html',{'data':data,'da':da})
def updateproduct(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pr = request.POST.get('price')
        qt = request.POST.get('quantity')
        ds = request.POST.get('discription')
        ct = request.POST.get('category')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = addproductdb.objects.get(id=dataid).Image
        addproductdb.objects.filter(id=dataid).update(Name=na,Price=pr,Quantity=qt,Discription=ds,Category=ct, Image=file)
        return redirect(displayproduct)

def logindata(request):
    return render(request,'loginpg.html')

def logindb_fun(request):
    if request.method == "POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpg)
            else:
                return redirect(logindata)
        else:
            return redirect(logindata)
def logout_fun(request):
    del request.session['username']
    del request.session['password']
    return redirect(indexpg)


def messagefu(request):
    data=messagedb.objects.all()
    return render(request,'displaymssg.html',{'data':data})








