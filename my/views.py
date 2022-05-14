from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ResgistrationForm

# Create your views here.
def index(request):
    return render(request, 'pages/my.html')
def contact(request):
    return render(request, 'pages/contact.html')
def blog(request):
    return render(request, 'pages/blog.html')
def register(request):
    form = ResgistrationForm()
    if request.method == 'POST':
        form = ResgistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    return render(request, 'pages/register.html', {'form': form})
    
        
