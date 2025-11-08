from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """
    Представление для отображения списка всех товаров
    """
    # Получаем все товары из базы данных
    products = Product.objects.all()
    
    # Создаем контекст для передачи в шаблон
    context = {
        'products': products,
        'title': 'Каталог товаров'
    }
    
    # Рендерим шаблон с контекстом
    return render(request, 'shop/product_list.html', context)

def product_detail(request, product_id):
    """
    Представление для отображения детальной информации о товаре
    """
    # Получаем товар по ID или возвращаем 404 если не найден
    product = get_object_or_404(Product, id=product_id)
    
    # Создаем контекст для передачи в шаблон
    context = {
        'product': product,
        'title': f'{product.name} - Детали'
    }
    
    # Рендерим шаблон с контекстом
    return render(request, 'shop/product_detail.html', context)
def catalog(request):
    """
    Представление для страницы каталога товаров
    """
    products = Product.objects.all()
    
    context = {
        'products': products,
        'title': 'Каталог товаров'
    }
    
    return render(request, 'shop/catalog.html', context)


