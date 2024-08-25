from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template, TemplateDoesNotExist
# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def greet(request, name):
    return render(request, 'hello/greet.html',{
        "name" : name.capitalize()
    })
    
def check_template(request):
    try:
        template = get_template('hello/greet.html')
        return HttpResponse(f'Template found at {template.origin.name}')
    except TemplateDoesNotExist:
        return HttpResponse('Template hello/greet.html does not exist')
    
def testttt(request):
    return render(request,"test.html")