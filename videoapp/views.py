from django.shortcuts import render
from .models import*
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.




def index(request) :
  if 'email' in request.session:
    
    uid =user.objects.get(email = request.session['email']) 
    
    context = {
      'uid' : uid
    }
    
    return render(request,"videoapp/index.html",context)
  else:
    return render(request, "videoapp/login.html")
  
def logout(request):
  if 'email' in request.session:
    del request.session['email']
    return render(request,"videoapp/login.html")
  else:
    return render(request,"videoapp/login.html")
   
  
def login(request):
   if 'email' in request.session:
     
     uid =user.objects.get(email = request.session['email']) 
    
     context = {
      'uid' : uid
     }
    
     return render(request,"videoapp/login.html",context)
   else:
      
      if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        
        uid=user.objects.get(email=email)
        request.session['email'] = uid.email
        if uid.email==email:
          if uid.password == password:  
          
            return render(request,'videoapp/index.html')
        else:
            return render(request,'videoapp/login.html')
      else:
            return render(request,'videoapp/login.html')
    
      
def about(request):
  return render (request,"videoapp/about.html")


def portfolio(request):
  return render (request,"videoapp/portfolio.html")

def services(request):
  return render (request,"videoapp/services.html")

def contact(request):
  
  if request.POST:
    email = request.POST['email']
    contact = request.POST['contact']
    message = request.POST['message']
    name = request.POST['name']
    
    
    cid = contact_up.objects.create(
      
                                  email = email,
                                  contact = contact,
                                  message = message,
                                  name = name

      
    )
    context = {
      
      'cid' : cid
    }
    
    return render (request,"videoapp/contact.html",context)
  else:
    return render(request,"videoapp/contact.html")
  

def blog_details(request):
 return render (request,"videoapp/blog-details.html")

def blog(request):
  return render (request,"videoapp/blog.html")

def register(request):
  
    
    if request.POST:
      
      email = request.POST['email']
      password = request.POST['password']
      username = request.POST['username']
      
      uid = user.objects.create(  email = email,
                                password = password,
                                username = username
                                
                                )
      
      context = {
        'uid' : uid
      }
      
      return render (request,"videoapp/register.html",context)
    else:
     return render (request,"videoapp/register.html")
   
def products(request):     
  uid = Add_product.objects.all()
   
  context ={
    
    'uid' : uid
    
  }
  
  
  return render(request,"videoapp/products.html",context)

def forget_password(request):
  if request.POST:
    email=request.POST['email']
    otp = random.randint(1111,9999)
    try:
      uid =user.objects.get(email=email)
      uid.otp=otp
      uid.save()
      send_mail ("forgot password", " your otp is" +str(otp), "gohiljayb10@gmail.com",[email])
      

      context ={
        'email' : email
      }
      return render(request,"videoapp/confirm.html",context)
    
    except:
      e_msg = "INVALID EMAIL"
      
      context = {
        'e_msg' : e_msg
      }
      
      return render (request,"vieoapp/forget_password.html",context)
    
  return render (request, "videoapp/forget_password.html")

def confirm(request):
  if request.POST:
    email = request.POST['email']
    otp = request.POST['otp']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    
    uid = user.objects.get(email=email)
    if str(uid.otp) == otp:
      if new_password == confirm_password:
        uid.password = new_password
        uid.save()
        
        context ={
          'email' : email
        }
        return render(request, "videoapp/login.html",context)
      else:
        context ={
          'p_msg' : "INVALID PASSWORD"
        }
        return render(request, "videoapp/confirm.html",context)
    else:
        
        e_msg = "INVALID OTP"  
        context ={
          'e_msg' : e_msg
        }
        return render(request, "videoapp/confirm.html",context)
      
  return render(request,"videoapp/confirm.html")
  
  



    
        
      
  

   
   








