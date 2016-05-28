from django.shortcuts import render
from blog.models import Post

#def post_list(request):
 #   return render(request, 'post_list.html', {})
def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

#    return render(request, 'blog/post_list.html', {})