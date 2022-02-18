from django.shortcuts import render, redirect
from . models import Post
from .forms import Postform

def home(request):
    return render(request, 'posts/index.html')

def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/posts.html', context)


def createpost(request):
    form = Postform()
    if request.method == 'POST':
        form=Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
        
    
    context = {'form':form}
    return render(request, 'posts/postforms.html', context)


