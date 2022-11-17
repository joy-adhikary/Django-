# from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hey joy welcome to the home page")
    

def hey(response):
    return HttpResponse("Hey joy welcome to the 2 page")
    