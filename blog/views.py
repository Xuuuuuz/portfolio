from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def Blog_page(request):
    blogs=Blog.objects
    return render(request,'blog.html',{'blogs':blogs})

def Blog_text(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'text.html', {'blog': blog})


