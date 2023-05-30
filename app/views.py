from django.shortcuts import render
from app.models import BlogPost, PortfolioPost

# Create your views here.
def blog(request):
    posts = BlogPost.objects.all()[:4]
    return render(request, 'app/blog.html', {"posts": posts})

def contact(request):
    return render(request, 'app/contact.html')

def index(request):
    return render(request, 'app/index.html')

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