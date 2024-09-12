from django.urls import path
from django.contrib.auth.decorators import login_required
from category.views import show_categories, show_category, Create_Category

urlpatterns = [
    path("", show_categories, name="categories.show"),
    path("<int:id>", show_category, name="category.show"),
    path("add_category", login_required(Create_Category.as_view()), name="category.create")
]

