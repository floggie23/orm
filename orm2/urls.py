from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('generate',views.generate),
    path('ninja',views.ninja),
    path('postdojo',views.postdojo),
    path('postninja',views.postninja)
]
