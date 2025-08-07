from django.shortcuts import render,redirect
from mirko.forms import ContactForm
from mirko.models import Service,PricingPlan
from restapi.models import Testimation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    services = Service.objects.all()
    planning = PricingPlan.objects.all()
    testing = Testimation.objects.all()
    print("hello",services)
    return render(request,"myapp/index.html",{'services':services,'planning':planning,'testing':testing})

   
def article(request):
    return render(request,'myapp/article.html')


def privacy(request):
    return render(request,'myapp/privacy.html')


def terms(request):
    return render(request,'myapp/terms.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'myapp/contact.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'myapp/login.html')

def logout_view(request):
      logout(request)
      return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'myapp/register.html', {'form': form})
