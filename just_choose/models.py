from django.db import models


# Create your models here.


class Restaurant(models.Model):
    # define a price range field for the Restaurant model; this field can only one of 4 values and is ££ by default
    LOW = '£'
    MODERATE = '££'
    HIGH = '£££'
    HIGHEST = '££££'
    # left side of the tuple is the value stored in the DB; right side is the text displayed to the user (i.e. in form)
    PRICE_RANGE_CHOICES = (
        (LOW, '£'),
        (MODERATE, '££'),
        (HIGH, '£££'),
        (HIGHEST, '££££'),
    )
    budget_range = models.CharField(
        max_length=4,
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
        ('indian', 'indian'),
        ('italian', 'italian'),
        ('mexican', 'mexican'),
        ('spanish', 'spanish'),
        ('chinese', 'chinese'),
        ('kebab', 'kebab'),
        ('greek', 'greek'),
        ('japanese', 'japanese'),
        ('american', 'american'),
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
        ('vegan', 'vegan'),
        ('vegetarian', 'vegetarian'),
        ('halal', 'halal'),
        ('kosher', 'kosher'),
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
        ('glu+mi', 'gluten,milk'),
        ('glu+nut', 'gluten,nuts'),
        ('mi+nut', 'milk,nuts'),
        ('glu+mi+nut', 'milk,nuts,gluten'),
        ('none', 'none')
    )
    allergy_warning = models.CharField(
        max_length=16,
        choices=ALLERGY_TYPE,
        default='none',
        null=True,
    )

    def __str__(self):
        return self.name
