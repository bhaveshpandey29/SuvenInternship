from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^index/', views.index, name = 'index'),
   url(r'^$', views.register, name = 'register'),
   url(r'^register/',views.register,name='register'),
   url(r'^details/(?P<id>\w{0,50})/$',views.details,name = 'details'),
   url(r'^add/',views.add, name='add'),
   url(r'^result/(?P<id>\w{0,50})/$',views.result, name='result'),

]