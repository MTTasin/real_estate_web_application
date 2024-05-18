from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def propertylist(request):
    return render(request, 'property-list.html')

def propertytype(request):
    return render(request, 'property-type.html')

def propertyagent(request):
    return render(request, 'property-agent.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def login(request):
    return render(request, 'login.html')