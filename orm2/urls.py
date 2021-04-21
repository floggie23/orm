from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('generate',views.generate),
    path('ninja',views.ninja),
    path('postdojo',views.postdojo),
    path('postninja',views.postninja),
    path('book',views.book),
    path('addbook',views.addbook),
    path('author',views.author),
    path('addauthor',views.addauthor), 
    path('author/<str:id>',views.viewauthor),
    path('book/<str:id>',views.viewbook),
    path('addbook/<str:id>',views.addab),
    path('addauthor/<str:id>',views.addba),
]
