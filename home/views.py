from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context={
        "joy":"joy adhikary",
        "joy2":"joy"
    }
    return render(request,'joy.html',context)
    # return HttpResponse("Hey joy welcome to the home page")


# load template one way 

def boot(request):
    return render(request,'bootstrap.html')

# load template another way 

def tem(request):
  template = loader.get_template('bootstrap.html')
  return HttpResponse(template.render())

def hey(request):
    return HttpResponse("Hey joy welcome to the second page")

def joy(request,dynamic_value):
    return HttpResponse(dynamic_value)