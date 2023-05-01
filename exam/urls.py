from django.urls import path
from . import views

urlpatterns = [
     path('', views.reference),
     path('prob/', views.St_List.as_view()),
     path('prob/<int:pk>/', views.St_Detail.as_view()),
     #('prob/', views.st_list),
     #path('prob/<int:pk>/', views.st_card),
 ]
