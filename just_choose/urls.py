from django.conf.urls import url
from just_choose import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact/$', views.contact, name ='contact'),
    url(r'^choose/$', views.choose, name ='choose'),
    url(r'^choose/dine/$', views.dine, name ='dine'),
    url(r'^choose/takeaway/$', views.takeaway, name ='takeaway'),
    url(r'^choose/takeaway/superchoose/$', views.superchoose, name ='superchoose'),
    url(r'^help/$', views.helper, name ='help'),
    url(r'^login/$', views.login, name ='login'),
    url(r'^profile/$', views.myprofile, name ='myprofile'),
    url(r'^signup/$', views.signup, name ='signup'),
 ]