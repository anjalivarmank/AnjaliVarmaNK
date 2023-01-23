from django.shortcuts import render,redirect
from StellarApp.models import categorydb,addproductdb,messagedb




# Create your views here.
def index1(request):
    data=categorydb.objects.all()
    return render(request,'index1.html',{'data':data})
def aboutpg(request):
    data = categorydb.objects.all()
    return render(request,'aboutus.html',{'data':data})
def contactpg(request):
    data = categorydb.objects.all()
    return render(request,'contactus.html',{'data':data})
def productpg(request):
    data=addproductdb.objects.all()
    return render(request,'product.html',{'data':data})

def discategory(request,itemcatg):
    data=addproductdb.objects.all()
    dat=categorydb.objects.all()
    print("===itemcatg===",itemcatg)
    catg=itemcatg.upper()
    products=addproductdb.objects.filter(Category=itemcatg)
    context={
        'products':products,
        'catg':catg,
        'da':data,
        'dat':dat
    }
    return render(request,"categorydisplay.html",context)

def prodetails(request,dataid):
    da=categorydb.objects.all()
    data = addproductdb.objects.get(id=dataid)
    return render(request, "productDetails.html", {'data': data,'da':da})

def messagefun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        obj=messagedb(Name=na,Email=em,Subject=sub,Message=msg)
        obj.save()
        return redirect(contactpg)






