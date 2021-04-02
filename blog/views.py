from django.shortcuts import render

from posts.models import Post, Author, Category
from marketing.models import Signup

# Create your views here.
def index(request):
    queryset = Post.objects.filter(featured=True)
    latest_post = Post.objects.filter(featured=True).order_by('-timestamp')[0:2]

    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    context ={
        "object_list": queryset,
        "latest": latest_post
    }
    return render(request, 'index.html' , context)

def blog(request):
    return render(request, 'blog.html')

def post(request):
    return render(request, 'post.html')