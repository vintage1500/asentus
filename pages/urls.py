from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pricing/', views.pricing_view, name='pricing'),

    path('about/', views.about_html, name='about'),

    path('products/', views.products_html, name='products'),

    path('faq/', views.faq_html, name='faq'),

    path('contact/', views.contact_html, name='contact')
]