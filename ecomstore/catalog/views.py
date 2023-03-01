from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from catalog.models import Category, Product


# Create your views here.
def catalog_home(request):
    return render(request, 'catalog/index.html',
                  context={'page_title': 'Musical Instruments and Sheet Music for Musicians'})


def show_category(request, category_slug):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    context = {
        'c': c,
        'products': products,
        'page_title': page_title,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }
    return render(request, 'catalog/category.html', context)


def show_product(request, product_slug):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    context = {
        'p': p,
        'categories': categories,
        'page_title': page_title,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
    }
    return render(request, 'catalog/product.html', context)
