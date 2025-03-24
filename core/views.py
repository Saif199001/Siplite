from django.shortcuts import render
from products.models import Product, Category, WholesaleCategory
from blog.models import BlogPost

def home(request):
    featured_products = Product.objects.all()[:6]  # Fetch 6 featured products
    latest_blogs = BlogPost.objects.all().order_by('-created_at')[:4]  # Fetch latest 4 blogs
    categories = Category.objects.all()  # Fetch Retail Categories
    wholesale_categories = WholesaleCategory.objects.all()  # Fetch Wholesale Categories

    return render(request, 'main/home.html', {
        'featured_products': featured_products,
        'latest_blogs': latest_blogs,
        'categories': categories,
        'wholesale_categories': wholesale_categories
    })
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def terms_conditions(request):
    return render(request, 'main/terms_conditions.html')