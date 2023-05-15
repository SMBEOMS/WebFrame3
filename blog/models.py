from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    class Meta:
        verbose_name_plural = 'Categories'




class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True) #요약문 필드만들기
    contents = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) #자동으로 작성 시각과 수정 시각 저장하기
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)  #이미지 폴더 지정하기
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)  #포스트에 파일 올리기
    #author: 추후 작성예정
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # on_delete=models.CASCAD

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    #category = models.ForeignKey(User, null=True, blank=True, on_delete=models.SxET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}' # self.pk = 해당 포스트의 pk 값, self.title = 해당 포스트의 title 값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]   #-1의미는 확장자 의미를함 EX) ~~.html txt py doc csv

