from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post, Author, Category
from marketing.models import Signup
from django.db.models import Q
# Create your views here.
def index(request):
    queryset = Post.objects.filter(featured=True),
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
    post_list= Post.objects.all()
    page_request_var = "page"
    paginator = Paginator(post_list, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    latest_post = Post.objects.filter(featured=True).order_by('-timestamp')[0:2]
    all_categories =  Category.objects.all()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context={
        "queryset" : paginated_queryset,
        "page_request_var": page_request_var,
        "most_recent": latest_post,
        "all_categories": all_categories,

    }
    return render(request, 'blog.html', context)

def post(request, pk):
    return render(request, 'post.html')


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)