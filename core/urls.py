from django.contrib import admin
from django.urls import path, include
from .views import home, about, contact, terms_conditions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),
    #path('faq/', faq, name='faq'),
    #path('testimonials/', testimonials, name='testimonials'),
    
    # Include Other Apps
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('users/', include('users.urls')),
    path('auth/', include('authentication.urls')),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
