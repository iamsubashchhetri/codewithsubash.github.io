# Create your views here.
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
 #return HttpResponse('this is home')
 return render(request, 'home.html')

def contact(request):
 #return HttpResponse('<h1>Page was found</h1>')
 return render(request, 'contact.html')
  
def about(request):
 #return HttpResponse('<h1>Page was found</h1>')
 return render(request, 'about.html')
  
def blog(request):
 #return HttpResponse('<h1>Page was found</h1>')
 return render(request, 'blog.html')
 