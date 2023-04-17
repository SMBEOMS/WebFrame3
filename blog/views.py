from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView): #index말고 class 로 정의 #클래스명을 파일명으로 자동으로바꾸어서 찾고있음
    model = Post #post_list 로 전달
    #template_name = 'blog/index.html'
    ordering = '-pk' 

class PostDetail(DetailView):
    model =  Post #등록되있는거 하나만 갖고옴
    template_name = 'blog/single_post_page.html'



# def index(request):
#     posts = Post.objects.all().order_by('-pk') #데이터베이스에 접근
#
#     return render(
#         request, 'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )
