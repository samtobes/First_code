from django.shortcuts import render,redirect
from .models import Post
from .forms import CreatePostForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

def postcreate(request):
    if request.method == "POST":
        form= CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your post has been added!!")
            return redirect("/")
            # return HttpResponse("Your post has been created")
    else:
        form= CreatePostForm()
    context={
        "form":form
    }
    return render(request, "blog/create_post.html",context)



def frontend_postcreate(request):
    if request.method=="POST":
        input_title=request.POST.get("title")
        input_content=request.POST.get("content")
        input_author=request.POST.get("author")
        user= User.objects.get(id=input_author)

        Post.objects.create(title=input_title,content=input_content,author=user)
        messages.success(request,"Your post has been added!!")
        return redirect("/")
    return render(request,"blog/frontend.html")
