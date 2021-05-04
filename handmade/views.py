from django.shortcuts import render, get_object_or_404
from .forms import SearchForm, ContactForm
from .models import Category, Product, Contact, Trends, Testimonial


def main(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    trends = Trends.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'main.html', {'categories': categories,
                                         'products': products, 'form': form,
                                         'trends': trends, 'testimonials': testimonials})


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'products.html', {'categories': categories,
                                             'products': products})


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})


def about(request):
    return render(request, 'about.html')


def company(request):
    return render(request, 'company.html')


def search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.filter(name=query)
    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
