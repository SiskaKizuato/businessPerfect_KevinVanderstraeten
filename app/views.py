from django.shortcuts import render, redirect
from app.models import BlogPost, PortfolioPost
from app.forms import BlogForm, PortfolioForm

# Create your views here.
def blog(request):
    posts = BlogPost.objects.all()[:4]
    return render(request, 'app/blog.html', {"posts": posts})

def contact(request):
    return render(request, 'app/contact.html')

def index(request):
    return render(request, 'app/index.html')

def backoffice(request):
    return render(request, 'app/backoffice/backoffice.html')

def portfolio(request):
    posts = PortfolioPost.objects.all()[:15]  # pour recup les 15 premiers articles
    images = [
        "app/img/portfolio-1.jpg",
        "app/img/portfolio-2.jpg",
        "app/img/portfolio-3.jpg",
        "app/img/portfolio-4.jpg",
        "app/img/portfolio-5.jpg",
        "app/img/portfolio-6.jpg",
        "app/img/portfolio-7.jpg",
        "app/img/portfolio-8.jpg",
        "app/img/portfolio-9.jpg",
        "app/img/portfolio-10.jpg",
        "app/img/portfolio-2.jpg",
        "app/img/portfolio-9.jpg",
        "app/img/portfolio-5.jpg",
        "app/img/portfolio-6.jpg",
        "app/img/portfolio-3.jpg",
    ]
    for post, image in zip(posts, images):
        post.image = image
    return render(request, "app/portfolio.html", {"posts": posts})


def create_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("portfolio")
    else:
        form = PortfolioForm()
    return render(request, "app/backoffice/create_portfolio.html", {"form": form})

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog")
    else:
        form = BlogForm()
    return render(request, "myApp/backoffice/create_blog.html", {"form": form})


def tableau(request):
    blogPost_list = BlogPost.objects.all()
    portfolioPost_list = PortfolioPost.objects.all()
    context = {
        "blogPost_list": blogPost_list,
        "portfolioPost_list": portfolioPost_list,
    }
    return render(request, "app/backoffice/tableau.html", context)