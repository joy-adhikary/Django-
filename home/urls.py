from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('y/', views.tem,name='inde'),
    path('x/', views.boot,name='ind'),
    path("xs", views.hey,name='hey'),
    path('<str:dynamic_value>', views.joy,name='joy'), 
    #eita holo dynamic value er syntax . doro amr onk gula course ashe . like 1 .... 100 akn amke 100 ta route create korty hobe joid manually kori tobe kintu course/1 ... course/100  jai dei nah kno amr sudu akbar ei function likhlei hocche 
    # tkn eita sudu course/1 ei 1 ke nibe and  1 er corosponding data show korbe 
]
