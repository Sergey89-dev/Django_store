from django.shortcuts import render
from .models import Product, ProductCategory
# Контролер задается функцией

def index(request): #  В качестве аргумента идет request
	context = {
		'title': 'Главная',
		'products': Product.objects.all()
	}
	return render(request, 'mainapp/index.html', context=context) #  Возвращается рендер из папки\

def contact(request):
	context = {
		'title': 'Контакты'
	}
	return render(request, 'mainapp/contact.html', context=context)


def products(request, pk=None):
	context = {
		'links_menu': ProductCategory.objects.all(),
		'title': 'Продукты'
	}
	return render(request, 'mainapp/products.html', context=context)

def main(request):
	title = 'Главная'
	products = Product.objects.all()[:4]

	content = {'title': title, 'products': products}
	return render(request, 'mainapp/index.html', content)