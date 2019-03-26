from django.conf.urls import url
from just_choose import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^choose/takeaway/$', views.takeaway, name='takeaway'),
    url(r'^login/$', auth_views.login, {'template_name': 'just_choose/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'just_choose/logout.html'}, name='logout'),
    url(r'^profile/$', views.myprofile, name='myprofile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^searches/$', views.searches, name='searches'),
    url(r'^takeaway/(?P<postcode>\w{1,50})/'r'(?P<cuisine>\w{1,50})/'r'(?P<budget_range>\w{1,50})/$', views.takeaway, name ='takeaway'),
    url(r'^dineout/(?P<postcode>\w{1,50})/'r'(?P<cuisine>\w{1,50})/'r'(?P<budget_range>\w{1,50})/$', views.dineout, name='dineout'),
    url(r'^menus/(?P<restaurant>\w{1,50})/$', views.menus, name='menus'),
    url(r'^restaurants/$', views.restaurants, name='restaurants'),
]
