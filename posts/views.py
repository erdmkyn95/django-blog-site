from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.shortcuts import render,HttpResponse
# Create your views here.

def base_link(request):
    return render(request, 'base_html/base.html', context={})

class PostListView(TemplateView):
    template_name = 'post/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all()[:5]
        return context