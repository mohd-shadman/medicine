from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import contactForm
from .forms import *
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    form= contactForm(request.POST or None)
    if form.is_valid():
        form_em=form.cleaned_data.get("email")
        form_mes=form.cleaned_data.get("message")
        form_name=form.cleaned_data.get("name")
        subject = 'Kind hearts medicine hub'
        from_email= settings.EMAIL_HOST_USER
        to_email=[form_em]
        # to_email=[from_email]
        contact_message= "%s: %s via %s"%(
            form_name,
            form_mes,
            form_em)
        
        try:
            send_mail(subject,contact_message,from_email,to_email)
        except BadHeaderError:
            return HttpResponse('invalid email not found')
        return redirect('success')
    # context = {
    #     "form" : form,
    # }
    return render(request,'contact.html',{'form':form})
     
def post(request):
    return render(request,'post.html')

def success(request):
    return render(request,'success.html')


def older(request):
    return render(request,'older.html')


def syrup(request):
    return render(request,'syrup.html')


def tablets(request):
    return render(request,'tablets.html')


def injection(request):
    return render(request,'injection.html')


def orders(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('booking')
    else:
        form=MedicineForm()
    return render(request,'orders.html',{'form1':form})

def booking(request):
    item = medicine.objects.all()
    return render(request,'booking.html',{'item':item})



def getvalue(request):
    if request.method=="POST":
        name=request.POST.get('name')
       
        brand=request.POST.get('brand')
        pic=request.POST.get('pic')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        quantity=request.POST.get('quantity')
        finalprice=request.POST.get('finalprice')
        total_price=request.POST.get('total_price')
        s=medicine(name=name,brand=brand,pic=pic,price=price,discount=discount,quantity=quantity,finalprice=finalprice,total_price=total_price)
        s.save()
        return redirect('/orders')
    # return render(request,'orders.html')