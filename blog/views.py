# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView, CreateView, UpdateView #CBV로 페이지 만들기
from .models import Post, Category




class PostList(ListView):
    model = Post
    ordering = '-pk' #ListView로 포스트 목록 페이지 만들기

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()  # post_list
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context  # -> post_list.html

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
            'post_list': post_list,

        }
    )
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): #form 기준
    model = Post
    fields = ['title', 'hook_text', 'contents', 'head_image', 'file_upload', 'category', 'tags']
    # template_name = post_form.html


    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            # not tag
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')
