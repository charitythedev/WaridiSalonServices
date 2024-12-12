from django.shortcuts import render, redirect

from application.forms import CustomerForm, ContactUsForm
from application.models import Service, Salon


# Create your views here.
def index(request):
    salons = Salon.objects.all()
    return render(request, 'index.html', {'salons': salons})

# Contact page
def contact(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('index')
    else:
        form = CustomerForm()
    return  render(request,'contact.html',{'form':form})


def services(request):
   data = Service.objects.all()
   return render(request, 'services.html',{'data':data})

def contactus(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactUsForm()
    return render(request, 'contact-us.html',{'contactor':form})