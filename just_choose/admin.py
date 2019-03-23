from django.contrib import admin
from just_choose.models import Restaurant, Menu, Profile
# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')

admin.site.register(Profile)
admin.site.register(Restaurant)
admin.site.register(Menu, MenuAdmin)
