from django.shortcuts import render,redirect
from .forms import updrink
from .models import drinks
from .models import customuser
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request,"home.html")
def Features(request):
    return render(request,"features.html")
def drinks(request):
    item=price.objects.all()
    return render(request,"drinks.html")
def Order(request):
    return render(request,"Order.html")
def price(request):
    uploads=updrink()
    if request.method=='POST':
        uploads=updrink(request.POST,request.FILES)
        if uploads.is_valid():
          uploads.save()
          return redirect('drks')
        else:
          return HttpResponse("""something went wrong.please reload webpage by clicking <a href="{{url:'pris'}}"> reload</a>""") 
    return render(request,"pricing.html",{'updr':uploads})
def createaccount(request):
    if request.method=="POST":
        fname=request.POST['FN'];
        lname=request.POST['LM'];
        email=request.POST['EM'];
        Psword=request.POST['PSW'];
        
        data=customuser.objects.create_user(F_Name= fname,L_Name=lname, E_Mail=email,Password=Psword)
        return redirect("logreg")
    return render(request,"createaccount.html")
# def SignIn(request):
#     if request.method=="POST":
#         print("hiii")
#         UserName=request.POST['email'] 
#         PassWord=request.POST['password'] 
#         user=authenticate(request,E_Mail=UserName,Password=PassWord) 
#         if user is not None:
#             login(request,user)
#             return redirect("pris")
#         else:
#             print("Invalid valid username or password")
#     return render(request,'Login.html')


     