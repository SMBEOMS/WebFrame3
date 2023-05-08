"""
URL configuration for do_it_django_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 미디어 파일을 위한 URL 지정하기
from django.conf.urls.static import static # 미디어 파일을 위한 URL 지정하기

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog.urls')), #FBV 스타일로 post_list페이지 만들기
    path('', include('single_pages.urls')),
    path('exam/', include('exam.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #admin 에서 이미지 주소를 누르면 설정됨