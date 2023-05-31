from django import forms
from .models import BlogPost, PortfolioPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioPost
        fields = '__all__'
