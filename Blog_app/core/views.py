from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Author,BlogPost 
from .forms import BlogForm

# Create your views here.

def home(request):
    blogs = BlogPost.objects.all()
    return render(request,'home_page.html',{'blogs':blogs})

def post_of_an_author(request,author):
    author_posts = BlogPost.objects.filter(author__name=author)
    return render(request,'author_posts.html',{'author_posts':author_posts})

def blog_details(request,pk):
    details = BlogPost.objects.get(pk=pk)
    return render(request,'details.html',{'blog':details})


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            published = request.POST['published_date']
            author = request.POST['author']
            BlogPost.create(title=title,content=content,publication_date=published,author=author)
            return redirect('/')
    else:
        form = BlogForm()
        
    return render(request,'add_blog.html',{'form':form})
        
    
    
