from django.urls import path

from . import views

app_name = 'blog_post'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('new/', views.CreatePost.as_view(), name='new_post'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
]
