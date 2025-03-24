from .models import Product, WholesaleCategory, WholesaleProduct, Category
from django.shortcuts import get_object_or_404, render

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        category = None

    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products,
        'selected_category': category
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products
    })



def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_products.html', {'category': category, 'products': products})

def wholesale_category_products(request, category_slug):
    category = get_object_or_404(WholesaleCategory, slug=category_slug)
    products = WholesaleProduct.objects.filter(category=category)
    return render(request, 'products/wholesale_category_products.html', {'category': category, 'products': products})
def wholesale_view(request):
    categories = WholesaleCategory.objects.all()
    category_products = {category: WholesaleProduct.objects.filter(category=category) for category in categories}

    return render(request, 'products/wholesale.html', {
        'categories': categories,
        'category_products': category_products
    })