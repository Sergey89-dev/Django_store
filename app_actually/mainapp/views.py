from django.shortcuts import render
# Контролер задается функцией

def index(request): #  В качестве аргумента идет request
	return render(request, 'mainapp/index.html') #  Возвращается рендер из папки\

def contact(request):
	return render(request, 'mainapp/contact.html')

links_menu = [
		{
			'url': 'products',
			'title': 'Все'
		},
		{
			'url': 'products_home',
			'title': 'дом'
		},
		{
			'url': 'products_office',
			'title': 'офис'
		},
		{
			'url': 'products_modern',
			'title': 'модерн'
		},
		{
			'url': 'products_classic',
			'title': 'классика'
		}
	]

def products(request):
	context = {
		'links_menu': links_menu
	}
	return render(request, 'mainapp/products.html', context=context)

def products_home(request):
	context = {
		'links_menu': links_menu
	}
	return render(request, 'mainapp/products.html', context=context)

def products_office(request):
	context = {
		'links_menu': links_menu
	}
	return render(request, 'mainapp/products.html', context=context)

def products_modern(request):
	context = {
		'links_menu': links_menu
	}
	return render(request, 'mainapp/products.html', context=context)

def products_classic(request):
	context = {
		'links_menu': links_menu
	}
	return render(request, 'mainapp/products.html', context=context)

