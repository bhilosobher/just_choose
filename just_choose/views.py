from django.http import HttpResponse
from just_choose.models import Restaurant
from just_choose.models import Menu
from just_choose.models import Profile
from just_choose.models import Search
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from just_choose.forms import SignUpForm
# Create your views here.


def index(request):
    cuisines = Restaurant.CUISINE_TYPES
    budget_ranges = Restaurant.PRICE_RANGE_CHOICES
    dict = {"cuisines" : cuisines, "budget_ranges" : budget_ranges}
    return render(request, 'just_choose/index_just_choose.html', dict)


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

def myprofile (request):
    return HttpResponse("once logged in, view profile")

def restaurants(request, postcode, cuisine, budget_range):
    restaurants = Restaurant.objects.filter(address=postcode)
    if (cuisine != "none"):
	    restaurants = restaurants.filter(cuisine=cuisine)
    else:
        cuisine = "All"
    if (budget_range != "none"):
	    restaurants = restaurants.filter(budget_range=budget_range)
    else:
        budget_range = -1
    dict = {"restaurants" : restaurants}
    if request.user.is_authenticated():
        profile = Profile.objects.filter(user=request.user).first()
        search = Search.objects.create(address=postcode, cuisine=cuisine, budget_range=budget_range)
        profile.searches.add(search)
    return render(request, 'just_choose/restaurants.html', dict)
	
def menus(request, restaurant):
    menus = Menu.objects.filter(restaurant__name=restaurant)
    serialized_menus = serializers.serialize('json', menus)
    return JsonResponse(serialized_menus, safe=False)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'just_choose/signup.html', {'form': form})

def searches(request):
    if request.user.is_authenticated():
        searches = Profile.objects.filter(user=request.user).first().searches.all()
        dict = {"searches" : searches}
        return render(request, 'just_choose/searches.html', dict)
    else:
        return render(request, 'just_choose/searches.html', {})
    