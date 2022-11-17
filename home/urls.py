from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('y/', views.tem,name='inde'),
    path('x/', views.boot,name='ind'),
    path("xs", views.hey,name='hey'),
    path('2/', views.joy,name='joy'),
    
]
