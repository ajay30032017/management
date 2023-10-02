import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
class SignUpView(generic.CreateView):
    form_class = UserCreationForm  #To create a form
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    
def index(request):
    return render(request,'scrapapp/home.html')

tarun = {}
def searchArea(request):
    data = json.loads(request.body)
    userType = data['searchpin']
    print(userType)
    global tarun
    tarun = userType
    print(tarun)    

    return JsonResponse('userselector',safe=False)

def buyer(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_total_items
        typeUser = userTypeModel.objects.all()
        add = Pickup.objects.all()
        Users = Customer.objects.all()
    else:
        order={}
        items ={}
        cartItem={}
        typeUser ={}
        add = {}
        
    
        
    context = {'order':order,'items':items,'cartItem':cartItem,'typeuser':typeUser,'address':add,'tarun':tarun,'users':Users}
    return render(request,'scrapapp/buyer.html',context)
def loginView(request):
    return render(request,'scrapapp/login.html')

def pickup(request):
   

    
   
    
    return render(request,'scrapapp/pickup.html')


def price(request):
    product = Product.objects.all()
    context = {'products':product}
    return render(request,'scrapapp/price.html',context)


def list(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_total_items
        add = Pickup.objects.all()
        
        
        
        
        
    
    
       
    
    else:
        order={}
        items ={}
        cartItem={}
        typeUser ={}
        
    
        
    context = {'order':order,'items':items,'cartItem':cartItem,'address':add}
    
    
    return render(request,'scrapapp/list.html',context)


def processOrder(request):
    data = json.loads(request.body)
    product =data['productID']
    action = data['action']
    
    print(product,action)
    
    return JsonResponse('hello',safe=False) 
    
def processRequest(request):
    data = json.loads(request.body)
    formdata = data['form']
    print(data)
    try:
        Pickup.objects.create(
        weight = formdata['weight'],
        date = formdata['date'],
        time = formdata['time'],
        address = formdata['address'],
        pincode = formdata['pincode']
        )
        
        print(Pickup['weight'])
    except:
        pass

    return JsonResponse('hell',safe=False)
    



def userType(request):
    data = json.loads(request.body)
    userType = data['formUser']
    print(userType)
    
    
    try:
        userTypeModel.objects.create(
            userType=userType['type'])
        
        
        
    except:
        print('buyer.name')
        pass
    
    
    
    
    
    

    return JsonResponse('userselector',safe=False)






    



    