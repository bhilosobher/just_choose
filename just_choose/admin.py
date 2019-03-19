from django.contrib import admin
from just_choose.models import Restaurant, Menu
# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')


admin.site.register(Restaurant)
admin.site.register(Menu, MenuAdmin)

