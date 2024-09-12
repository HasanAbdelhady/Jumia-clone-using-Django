from django.urls import path
from django.contrib.auth.decorators import login_required
from products.views import products, show_product, delete_from_db, add_product, edit_product, CreateProduct
urlpatterns = [
    path('', products, name="products.index"),
    path('<int:id>', show_product, name="one_product.index"),
    path('delete/<int:id>', login_required(delete_from_db), name='products.delete'),
    path('add_product', login_required(CreateProduct.as_view()), name='products.add'),
    path('edit/<int:id>/', login_required(edit_product), name='product.edit'),
]
    