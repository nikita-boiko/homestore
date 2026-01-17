from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',

    }


    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классный и какой хороший товар.'
        
    }


    return render(request, 'main/about.html', context)

def contacts(request):
    context = {
        'title': 'Home - Контактная ифнормация',
        'content': 'Контактная ифнормация',
        'text_on_page': 'Järve tornid, Järve tn 2, Таллинн, 11314. Часы работы салона: Пн-Пт 9-18, Сб 10-15.Тел.: +372 601 1441 Моб.: +372 51 999 622Эл. почта: info@alexanto.ee'
        
    }


    return render(request, 'main/contacts.html', context)

def deliver(request):
    context = {
        'title': 'Home - Доставка и оплата',
        'content': 'Доставка и оплата',
        'delivery_info': ' Доставка: по Таллинну от 50€ бесплатно (1-2 дня), по Эстонии от 100€ бесплатно (2-3 дня). Оплата: картой онлайн, наличными/картой при получении, рассрочка 0% на 3 месяца. Самовывоз: Järve tn 2, Таллинн. Тел: +372 601 1441'
        
    }


    return render(request, 'main/deliver.html', context)
