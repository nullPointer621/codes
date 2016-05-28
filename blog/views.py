from django.shortcuts import render
from blog.models import Post
from .forms import PostForm
from django.http import HttpResponse


#def post_list(request):
 #   return render(request, 'post_list.html', {})
def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Success")
		else:
			return render(request, 'post_edit.html', {'form': form})
	else:
		form  =  PostForm()

	return render(request, 'post_edit.html', {'form': form})


#    return render(request, 'blog/post_list.html', {})