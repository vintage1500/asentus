from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'pages/index.html')


def pricing_view(request):
    return render(request, 'pages/pricing.html')


def about_html(request):
    return render(request, 'pages/about.html')


def products_html(request):
    return render(request, 'pages/products.html')


def faq_html(request):
    return render(request, 'pages/faq.html')


def contact_html(request):
    return render(request, 'pages/contact.html')
