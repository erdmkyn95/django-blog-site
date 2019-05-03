from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.shortcuts import render,HttpResponse
# Create your views here.

def base_link(request):
    return render(request, 'base_html/base.html', context={})

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'