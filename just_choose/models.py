from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    # define a price range field for the Restaurant model; this field can only one of 4 values and is ££ by default
    LOW = 1
    MODERATE = 2
    EXPENSIVE = 3
    LUX = 4
    # left side of the tuple is the value stored in the DB; right side is the text displayed to the user (i.e. in form)
    PRICE_RANGE_CHOICES = (
        (LOW, '£'),
        (MODERATE, '££'),
        (EXPENSIVE, '£££'),
        (LUX, '££££'),
    )
    budget_range = models.IntegerField(
        choices=PRICE_RANGE_CHOICES,
        default=MODERATE,
        blank=False,
    )

    name = models.CharField(
        max_length=128,
        unique=True,
    )
    # define another choice field for the restaurant: this one can take as many values as the cuisine tuple has below
    CUISINE_TYPES = (
        ('indian', 'Indian'),
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('spanish', 'Spanish'),
        ('chinese', 'Chinese'),
        ('kebab', 'Kebab'),
        ('greek', 'Greek'),
        ('japanese', 'Japanese'),
        ('american', 'American'),
        ('eclectic', 'eclectic'),
    )

    cuisine = models.CharField(
        max_length=32,
        choices=CUISINE_TYPES,
        blank=False,
        default='eclectic',
    )

    address = models.CharField(
        max_length=8,
        blank=False,
    )
    
	#restaurants that have the option to dine out
    dine_out = models.BooleanField(default=True)
	
	#restaurants that offer take away
    take_away= models.BooleanField(default=True)

    #restaurants that have paid a fee in order to be promoted on the front page
    promoted= models.BooleanField(default=False)

    # some restaurants may link their websites, others not
    website = models.URLField(
        max_length=200,
        null=True,
        blank=True,
    )

    # some restaurants may have a delivery fee listed, others not.
    delivery_fee = models.FloatField(
        max_length=8,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    # second table: contains items, which references restaurants (thus constituting each restaraunt's menu)


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=128,
        unique=True,
    )
    ITEM_TYPE = (
        ('starter', 'starter'),
        ('main', 'main'),
        ('dessert', 'dessert'),
        ('side', 'side'),
        ('drink', 'drink'),
        ('deal', 'deal'),
    )
    type = models.CharField(
        max_length=8,
        choices=ITEM_TYPE,
        blank=True,
        null=True,
    )
    price = models.FloatField(
        null=True,
        max_length=10,
    )
    DIETARY_TYPE = (
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('halal', 'Halal'),
        ('kosher', 'Kosher'),
        ('none', 'none'),
    )
    dietary_mentions = models.CharField(
        max_length=10,
        choices=DIETARY_TYPE,
        blank=True,
        default='none',
    )
    ALLERGY_TYPE = (
        ('nuts', 'nuts'),
        ('milk', 'milk'),
        ('gluten', 'gluten'),
        ('glu+mi', 'gluten, milk'),
        ('glu+nut', 'gluten, nuts'),
        ('mi+nut', 'milk, nuts'),
        ('glu+mi+nut', 'milk, nuts, gluten'),
        ('none', 'none')
    )
    allergy_warning = models.CharField(
        max_length=16,
        choices=ALLERGY_TYPE,
        default='none',
        blank=True,
    )

    def __str__(self):
        return self.name

class Search(models.Model):
    address = models.CharField(
        max_length=8,
        blank=False,
    )
    cuisine = models.CharField(
        max_length=32,
        choices=Restaurant.CUISINE_TYPES,
        blank=True,
    )
    budget_range = models.IntegerField(
        choices=Restaurant.PRICE_RANGE_CHOICES,
        blank=True,
    )
    def __str__(self):
        return '%s| %s| %s' % (self.address, self.cuisine, self.budget_range)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    searches = models.ManyToManyField(Search, blank=True)

    def __str__(self):
        return self.user.username