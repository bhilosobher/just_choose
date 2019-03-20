from django.shortcuts import render
from django.http import HttpResponse
from just_choose.models import Restaurant
from just_choose.models import Menu
from django.http import JsonResponse
from django.core import serializers
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


def restaurants(request, postcode):
    restaurants = Restaurant.objects.filter(address=postcode)
    serialized_restaurants = serializers.serialize('json', restaurants)
    return JsonResponse(serialized_restaurants, safe=False)
	
def menus(request, restaurant):
    menus = Menu.objects.filter(restaurant__name=restaurant)
    serialized_menus = serializers.serialize('json', menus)
    return JsonResponse(serialized_menus, safe=False)