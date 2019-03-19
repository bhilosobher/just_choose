from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'just_choose/index_just_choose.html', {})


def contact(request):
    return HttpResponse("This is the contact us/about us page!")


def choose(request):
    return HttpResponse("here you choose between takeaway and restaurant wheel")


def dine (request):
    return HttpResponse("This is the wheel for dining out w/ dining out customization options!")


def takeaway (request):
    return HttpResponse("This is the wheel for dining out w/ dining out customization options!")


def superchoose (request):
    return HttpResponse("here you have to option to spin for a random meal")


def helper (request):
    return HttpResponse("if you need help..")


def login (request):
    return HttpResponse("login")


def myprofile (request):
    return HttpResponse("once logged in, view profile")


def signup (request):
    return HttpResponse("register!")
