
from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('privacy',views.privacy,name="privacy"),
    path('terms',views.terms,name="terms"),
    path('details/<int:pk>',views.details,name="details"),
    path('about',views.about,name="about"),
    path('search',views.search,name="search"),
    path('for-sale',views.for_sale,name="for_sale"),
    path('for-rent',views.for_rent,name="for_rent"),
    path('message',views.message,name="message"),
    path('order',views.order,name="order"),
]
