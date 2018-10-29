from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    url(r'^ajax/get_item/$', views.get_item, name='get_item'),
    url(r'^ajax/mark_correct/$', views.mark_correct, name='mark_correct'),
    url(r'^ajax/mark_incorrect/$', views.mark_incorrect, name='mark_incorrect'),
    path('lists/', views.lists, name='lists'),
    url(r'^list/(?P<pk>\d+)/$', views.list_view, name='list_view'),
    url(r'^list/edit/(?P<pk>\d+)/$', views.list_edit, name='list_edit'),
    path('list_create', views.list_create, name='list_create'),
    url(r'^list_remove/(?P<pk>\d+)/$', views.list_remove, name='list_remove'),
    path('items/', views.items, name='items'),
    url(r'^item/(?P<pk>\d+)/$', views.item_view, name='item_view'),
    url(r'^item/edit/(?P<pk>\d+)/$', views.item_edit, name='item_edit'),
    path('item/create', views.item_create, name='item_create'),
    url(r'^item/create/(?P<pk>\d+)/$', views.item_create, name='item_create'),
    url(r'^item_remove/(?P<pk>\d+)/$', views.item_remove, name='item_remove'),
    path('account/', views.account, name='account'),
    url(r'^account/reset_stats/(?P<pk>\d+)/$', views.reset_stats, name='reset_stats'),
    path('register/', views.register, name='register'),
    path('help/', views.help, name='help'),
    path('error/', views.error, name='error'),
    path('home/', views.home, name='home'),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
