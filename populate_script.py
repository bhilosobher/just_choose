import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ITECH_project.settings')

import django
django.setup()
from just_choose.models import Restaurant, Menu, Search, Profile


def populate():
    
    menu_items = [
		{"name": "Chicken tikka", "type":"main", "price": 8, "dietary":"halal", "allergy":"milk"},
		{"name": "Quatro stagioni", "type":"main", "price": 7, "dietary":"none", "allergy":"gluten"},
	    {"name": "Kebab", "type":"main", "price": 12 , "dietary":"halal", "allergy":"milk"},
        {"name": "Burrito", "type":"main", "price": 2, "dietary":"none", "allergy":"mi+nut"},
        {"name": "sandwich", "type":"main", "price": 3, "dietary":"none", "allergy":"glu+nut"},
        {"name": "potato", "type":"main", "price": 5, "dietary":"none", "allergy":"none"},
        {"name": "bread", "type":"main", "price": 6, "dietary":"kosher", "allergy":"glu+mi+nut"},
        {"name": "shaworma", "type":"main", "price": 7, "dietary":"kosher", "allergy":"glu+mi"},
        {"name": "chips", "type":"side", "price": 8, "dietary":"kosher", "allergy":"nuts"},
        {"name": "naan", "type":"side", "price": 9, "dietary":"kosher", "allergy":"mi+nut"},
        {"name": "pancakes", "type":"dessert", "price": 12, "dietary":"vegetarian", "allergy":"none"},
        {"name": "salad", "type":"deal", "price": 23, "dietary":"vegetarian", "allergy":"milk"},
        {"name": "pepsi", "type":"drink", "price": 1, "dietary":"vegetarian", "allergy":"none"},
        {"name": "family deal", "type":"deal", "price": 23, "dietary":"vegetarian", "allergy":"nuts"},
        {"name": "family feast", "type":"deal", "price": 32, "dietary":"vegetarian", "allergy":"none"},
        {"name": "more salad", "type":"main", "price": 13, "dietary":"vegetarian", "allergy":"none"},
        {"name": "Prosecco", "type":"drink", "price": 14, "dietary":"vegan", "allergy":"none"},
        {"name": "rice", "type":"side", "price": 4, "dietary":"vegan", "allergy":"none"},
        {"name": "vegetables", "type":"side", "price": 7, "dietary":"vegan", "allergy":"none"},
        ]
    
 
    # pages = items; x_pages = menu_items; 
    restaurants = {
        "restaurant name": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G12 8QQ","delivery_fee":2},
        "ashoka": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G1 8RE","delivery_fee":2},
        "bibimbap": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G2 4HR","delivery_fee":2},
        "chicken place": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G1 3SE","delivery_fee":2},
        "mamafubu": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G3 4AW","delivery_fee":2},
        "cafe india": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G13 5AS","delivery_fee":2},
        "nam tuk": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G5 5EQ","delivery_fee":2},
        "taco mazama": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G20 0DA","delivery_fee":2},
        "mong kok": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G20 0HR","delivery_fee":2},
        "tribecca": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G20 8PW","delivery_fee":2},
        "pizza hut": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G22 7PQ","delivery_fee":2},
        "dominos": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G31 4ER","delivery_fee":2},
        "byblos": {"items": menu_items, "budget": 1,  "cuisine":"indian","address":"G41 4RE","delivery_fee":2},
        "barburrito": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G31 9RE","delivery_fee":2},
        "wetherspoons": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G51 4RE","delivery_fee":2},
        "monte carlo": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G5 5RE","delivery_fee":2},
        "mamma mia": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G5 K33","delivery_fee":2},
        "buena vista": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G11 4TT","delivery_fee":2},
        "pickled ginger": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G12 4SD","delivery_fee":2},
        "yen": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G11 4RF","delivery_fee":2},
        "best kebab": {"items": menu_items, "budget": 1,  "cuisine":"italian","address":"G11 4FS","delivery_fee":2},
        "marakech": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G40 4EE","delivery_fee":2},
        "chippie": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G71 3DS","delivery_fee":2},
        "marcos": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G14 45S","delivery_fee":2},
        "stake and cherry": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G13 3DE","delivery_fee":2},
        "satu stau": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G20 34R","delivery_fee":2},
        "mother india": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G5 3EW","delivery_fee":2},
        "mcdonalds": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G3 4DS","delivery_fee":2},
        "another restaurant": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G3 8SW","delivery_fee":2},
        "kfc": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G3 5AA","delivery_fee":2},
        "idea": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G1 5SS","delivery_fee":2},
        "roasted python": {"items": menu_items, "budget": 1,  "cuisine":"mexican","address":"G2 3SS","delivery_fee":2},
        "grilicious": {"items": menu_items, "budget": 1,  "cuisine":"spanish","address":"G14 RSS","delivery_fee":2},
        "pepes": {"items": menu_items, "budget": 1,  "cuisine":"american","address":"G1 1QQ","delivery_fee":2},
        "chunky chiken": {"items": menu_items, "budget": 1,  "cuisine":"spanish","address":"G2 4DD","delivery_fee":2},
        "burgers and co": {"items": menu_items, "budget": 1,  "cuisine":"spanish","address":"G3 3FF","delivery_fee":2},
        "bread meats bread": {"items": menu_items, "budget": 1,  "cuisine":"spanish","address":"G12 3KD","delivery_fee":2},
        "scoop and loop": {"items": menu_items, "budget": 1,  "cuisine":"spanish","address":"G11 4HR","delivery_fee":2},
        "decent sweets": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G4 3SD","delivery_fee":2},
        "pizza punks": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G4 3AE","delivery_fee":2},
        "subway": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G40 4WW","delivery_fee":2},
        "americano": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G50 3SD","delivery_fee":2},
        "dumpling monkey": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G51 D34","delivery_fee":2},
        "banana leaf": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G50 3FF","delivery_fee":2},
        "pinnnochio": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G5 6SS","delivery_fee":2},
        "django on bread": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G22 5RR","delivery_fee":2},
        "we love django": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G20 4RT","delivery_fee":2},
        "best restaurant name": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G12 5RC","delivery_fee":2},
        "animalx": {"items": menu_items, "budget": 1,  "cuisine":"chinese","address":"G1 4DF","delivery_fee":2},
        "inn deep": {"items": menu_items, "budget": 1,  "cuisine":"kebab","address":"G2 2ER","delivery_fee":2},
        "caledonian": {"items": menu_items, "budget": 1,  "cuisine":"kebab","address":"G3 5HF","delivery_fee":2},
        "cuib": {"items": menu_items, "budget": 1,  "cuisine":"kebab","address":"G4 5DS","delivery_fee":2},
        "retro": {"items": menu_items, "budget": 1,  "cuisine":"kebab","address":"G1 4HD","delivery_fee":2},
        "cafe paridiso": {"items": menu_items, "budget": 1,  "cuisine":"greek","address":"G4 4SD","delivery_fee":2},
        "salt'n'peppa": {"items": menu_items, "budget": 1,  "cuisine":"greek","address":"G4 4GH","delivery_fee":2},
        "winrar": {"items": menu_items, "budget": 1,  "cuisine":"greek","address":"G5 5FG","delivery_fee":2},
        "game of thrones": {"items": menu_items, "budget": 1,  "cuisine":"greek","address":"G3 4VD","delivery_fee":2},
        "supper and pupper": {"items": menu_items, "budget": 1,  "cuisine":"greek","address":"G71 4SS","delivery_fee":2},
        "getting there": {"items": menu_items, "budget": 1,  "cuisine":"japanese","address":"G12 4GG","delivery_fee":2},
        "blue lagoon": {"items": menu_items, "budget": 1,  "cuisine":"japanese","address":"G11 5HG","delivery_fee":2},
        "koh i noor": {"items": menu_items, "budget": 1,  "cuisine":"japanese","address":"G2 23R","delivery_fee":2},
        "the gardner": {"items": menu_items, "budget": 1,  "cuisine":"american","address":"G1 1RT","delivery_fee":2},
        "hillhead bookclub": {"items": menu_items, "budget": 1,  "cuisine":"eclectic","address":"G1 5HF","delivery_fee":2},
        "jamie's italian": {"items": menu_items, "budget": 1,  "cuisine":"eclectic","address":"G4 4SS","delivery_fee":2},
        "michellin": {"items": menu_items, "budget": 1,  "cuisine":"eclectic","address":"G3 3WW","delivery_fee":2},
        "end of days": {"items": menu_items, "budget": 1,  "cuisine":"eclectic","address":"G1 1AA","delivery_fee":2},
        }
    
  
	# The code below goes through the restaurants dictionary, then adds the same items to each restaurant's menu
	# then adds the same items to each restaurant's men


    for rest, rest_data in restaurants.items():
        r = add_restaurant(rest, rest_data["budget"], rest_data["cuisine"],rest_data["address"],rest_data["delivery_fee"])
        for i in rest_data["items"]:
            add_item(r, i["name"], i["type"], i["price"], i["dietary"],i["allergy"])

#(for debug)rango version of the above^:
#    for cat, cat_data in cats.items():
#        c = add_cat(cat, cat_data["views"], cat_data["likes"])
#        for p in cat_data["pages"]:
#            add_page(c, p["title"], p["url"], p["views"])
    
    # Print out what we have added to the user.

    for r in Restaurant.objects.all():
        for i in Menu.objects.filter(restaurant=r):
            print("- {0} - {1}".format(str(r), str(i)))

    #rango version of the above^:
    #for c in Category.objects.all():
    #    for p in Page.objects.filter(category=c):
    #        print("- {0} - {1}".format(str(c), str(p)))


def add_item(rest, name, type, price, dietary = "none", allergy = "none"):
    i = Menu.objects.get_or_create(restaurant=rest, name=name)[0]
    i.type = type
    i.price = price
    i.dietary_mentions = dietary
    i.allergy_warning = allergy
    i.save()
    return i

#rango version, for debug
#def add_page(cat, title, url, views=0):
#    p = Page.objects.get_or_create(category=cat, title=title)[0]
#    p.url=url
#    p.views=views
#    # we need to save the changes we made!!
#    p.save()
#    return p

def add_restaurant(name, budget, cuisine, address, delivery_fee):
    r = Restaurant.objects.get_or_create(name=name, address = address)[0]
    r.budget = budget
    r.cuisine = cuisine,
    r.delivery_fee = delivery_fee
    r.save()
    return r

#rango version, for debug
#def add_cat(name, views=0, likes=0):
#    c = Category.objects.get_or_create(name=name)[0]
#    c.views=views
#    c.likes=likes
#    c.save()
#    return c



# Start execution here!
if __name__ == '__main__':
    print("Starting Just Choose population script...")
    populate()