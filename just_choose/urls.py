from django.conf.urls import url
from just_choose import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact/$', views.contact, name ='contact'),
    url(r'^choose/$', views.choose, name ='choose'),
    url(r'^choose/dine/$', views.dine, name ='dine'),
    url(r'^choose/takeaway/$', views.takeaway, name ='takeaway'),
    url(r'^choose/takeaway/superchoose/$', views.superchoose, name ='superchoose'),
    url(r'^help/$', views.helper, name ='help'),
    url(r'^login/$', auth_views.login, {'template_name': 'just_choose/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'just_choose/logout.html'}, name='logout'),
    url(r'^profile/$', views.myprofile, name ='myprofile'),
    url(r'^signup/$', views.signup, name='signup'),
	url(r'^searches/$', views.searches, name='searches'),
	url(r'^restaurants/(?P<postcode>\w{1,50})/'r'(?P<cuisine>\w{1,50})/'r'(?P<budget_range>\w{1,50})/$', views.restaurants, name ='restaurants'),
	url(r'^menus/(?P<restaurant>\w{1,50})/$', views.menus, name ='menus'),
 ]