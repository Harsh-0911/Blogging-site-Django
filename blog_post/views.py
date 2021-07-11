from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm


class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        form = ArticleForm(initial={'author':request.user})
        ctx = {
            'form': form,
        }
        return render(request, 'blog_post/new_post.html', ctx)

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_post:article_list')

        ctx = {
            'form': form,
        }
        return render(request, 'blog_post/new_post.html', ctx)


class ArticleList(LoginRequiredMixin, ListView):
    queryset = Article.objects.order_by('-created_on')[:10]
    template_name = 'blog_post/article_list.html'


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'blog_post/article_detail.html'
