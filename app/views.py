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
    return render(request, 'app/portfolio.html')