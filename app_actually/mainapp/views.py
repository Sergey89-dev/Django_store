from django.shortcuts import render
# Контролер задается функцией

def index(request): #  В качестве аргумента идет request
	context = {
		'title': 'Главная'
	}
	return render(request, 'mainapp/index.html', context=context) #  Возвращается рендер из папки\

def contact(request):
	context = {
		'title': 'Контакты'
	}
	return render(request, 'mainapp/contact.html', context=context)

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
		'links_menu': links_menu,
		'title': 'Продукты'
	}
	return render(request, 'mainapp/products.html', context=context)

def products_home(request):
	context = {
		'links_menu': links_menu,
		'title': 'Мебель для дома'
	}
	return render(request, 'mainapp/products.html', context=context)

def products_office(request):
	context = {
		'links_menu': links_menu,
		'title': 'мебель для офиса'
	}
	return render(request, 'mainapp/products.html', context=context)

def products_modern(request):
	context = {
		'links_menu': links_menu,
		'title': 'Современная мебель'
	}
	return render(request, 'mainapp/products.html', context=context)

def products_classic(request):
	context = {
		'links_menu': links_menu,
		'title': 'Классическая мебель'
	}
	return render(request, 'mainapp/products.html', context=context)

