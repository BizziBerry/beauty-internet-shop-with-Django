// JavaScript для интернет-магазина
console.log('Интернет-магазин загружен!');

// Можно добавить функциональность для корзины, фильтров и т.д.
document.addEventListener('DOMContentLoaded', function() {
    // Пример: обработка кнопки "Добавить в корзину"
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            alert('Товар добавлен в корзину!');
        });
    });
});
