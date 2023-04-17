from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('',views.index),
    #path('<int:pk>/', views.single_post_page), #bolg/숫자 넣어야 함
    path('',views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]
#pk = 숫자
