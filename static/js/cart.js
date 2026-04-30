document.addEventListener('DOMContentLoaded', function () {

    const buttons = document.querySelectorAll('.add-to-cart-btn');

    buttons.forEach(button => {
        button.addEventListener('click', function () {

            const productId = this.dataset.productId;

            fetch(`/cart/add/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {

                if (data.success) {

                    const cartBadge = document.querySelector('.badge');

                    if (cartBadge) {
                        cartBadge.textContent = data.cart_count;
                    }

                    this.textContent = '✔ Добавлено';
                    this.classList.remove('btn-success');
                    this.classList.add('btn-secondary');

                    // 🔥 TOAST
                    const toastElement = document.getElementById('cartToast');

                    if (toastElement) {
                        const toast = new bootstrap.Toast(toastElement);
                        toast.show();
                    }

                    setTimeout(() => {
                        this.textContent = 'В корзину';
                        this.classList.remove('btn-secondary');
                        this.classList.add('btn-success');
                    }, 1500);
                }
            });
        });
    });

});