from .forms import PostForm
from .models import Post
from django.contrib import auth
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def homepage(request):
	return render(request, 'homepage.html')

def gallery(request):
	return render(request, 'gallery.html')

def about(request):
	return render(request, 'about.html')

def story(request):
	posts = Post.objects.all()
	return render(request, 'story.html', {'posts': posts})

def account(request):
	posts = Post.objects.all()
	return render(request, 'account.html', {'posts': posts})

def story_detail(request, pk ):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'story_detail.html',{'post': post})

def new_story(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.writer = request.user
			post.posted_date = timezone.now()
			post.save()
			return redirect('story_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'new_story.html', {'form':form})

def edit_story(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.posted_date = timezone.now()
            post.save()
            return redirect('story_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'new_story.html', {'form': form})
	

