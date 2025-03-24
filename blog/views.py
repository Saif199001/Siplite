from django.shortcuts import render, get_object_or_404
from .models import BlogPost
def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')  # Fetch blogs in descending order
    return render(request, 'blog/blog_list.html', {'blogs': blogs})
def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    related_blogs = BlogPost.objects.exclude(id=blog.id).order_by('-created_at')[:3]  # Fetch 3 related blogs
    
    return render(request, 'blog/blog_detail.html', {
        'blog': blog,
        'related_blogs': related_blogs
    })