# from django.shortcuts import render
from django.views.generic import ListView,DetailView #CBV로 페이지 만들기
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk' #ListView로 포스트 목록 페이지 만들기

class PostDetail(DetailView):
    model = Post

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html', #사용할 템플릿
#         {
#             'post' : post, #템플릿에 넘겨줄 값 딕셔너리 형태로.
#         }
#     )
# Create your views here.
# def index(request):#FBV 스타일로 post_list페이지 만들기
#     posts = Post.objects.all().order_by('-pk')
#     #쿼리로 Post 목록 가져오기 (데이터베이스) 모델명.objects.all() 모든 post를 가져옴
#     #.order_by('-pk') = 역순으로 나열
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )