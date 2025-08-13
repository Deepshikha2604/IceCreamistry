from django.shortcuts import render
from django.http import HttpResponse
from .models import chef
from .models import iceCream
from .models import Services
from userApp.models import profile
from .models import contact
# Create your views here.
def home(request):
    chefData=chef.objects.all()
    print(chefData)
    context={'chefData':chefData}
    return render(request,'products/home.html',context)

def productPage(request):
    iceCreamData=iceCream.objects.all()
    context={'iceCreamData':iceCreamData}
    return render(request, 'products/productPage.html',context)

def aboutPage(request):
    chefData=chef.objects.all()
    print(chefData)
    context={'chefData':chefData}
    return render(request, 'products/about.html',context )

def ServicePage(request):
    ServiceData=Services.objects.all()
    ClientData=profile.objects.all()
    print(ServiceData)
    print(ClientData)
    context={'service':ServiceData, 'profile':ClientData}
    return render(request, 'products/ServicePage.html',context )

def contactPage(request):
    if request.method=='POST':
        contact_name=request.POST.get('name')
        contact_email=request.POST.get('email')
        contact_subject=request.POST.get('subject')
        contact_query=request.POST.get('message')

        contactUs=contact(contact_name=contact_name, contact_email=contact_email, contact_subject=contact_subject, contact_query=contact_query)
        contactUs.save()
        
    # contactData=contact.objects.all()
    # print(contactData)
    # context={'contactData':contactData}
    return render(request, 'products/contactPage.html' )
