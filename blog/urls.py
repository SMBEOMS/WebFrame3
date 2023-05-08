from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    #path('', views.index), #FBV 스타일로 post_list페이지 만들기
    #path('<int:pk>/', views.single_post_page), #FBV로 post_detail 페이지 만들기
    ]