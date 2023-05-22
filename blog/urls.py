from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create_post/', views.PostCreate.as_view()),
    #path('update_post/<int:pk>', views.PostUpdate.as_view()),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page),
    #path('', views.index), #FBV 스타일로 post_list페이지 만들기
    #path('<int:pk>/', views.single_post_page), #FBV로 post_detail 페이지 만들기
    ]