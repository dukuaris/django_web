"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include   # include 추가
from mysite.views import HomeView # 추가

# from bookmark.views import BookmarkLV, BookmarkDV  # 삭제

urlpatterns = [
    path('admin/', admin.site.urls),
    # shkim
    path('', HomeView.as_view(), name='home'),  #추가
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),


    # 기존 3개 라인 삭제
    #class-based views
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
