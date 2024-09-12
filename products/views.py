from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.urls import reverse_lazy
from products.models import Product
from products.forms import ProductForm
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

def is_superuser(user):
    return user.is_superuser

def products(request):
    products = Product.objects.all().order_by('id')
    return render(request, template_name="products/products.html", context={"products":products})


def show_product(request, id):
    products = Product.objects.all()
    product = get_object_or_404(products, id=id)
    return render(request, template_name="products/product.html", context={"product":product})

def delete_from_db(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    url = reverse("products.index")
    return  redirect(url)

def add_product(request, id=None):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            product = form.save()
            url = reverse("one_product.index", args=[product.id])
            return redirect(url)
    return render(request, 'products/add_product.html', {"product_form": form})

@method_decorator([login_required, user_passes_test(is_superuser, login_url=reverse_lazy('products.index'))], name='dispatch')
class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'

    def form_valid(self, form):
        if form.is_valid():
            product = form.save(commit=False)
            product.user = self.request.user 
            product.save()
            return redirect('products.index')


@login_required
def edit_product(request, id):
    if request.user.is_superuser:
        product = get_object_or_404(Product, id=id)
        form = ProductForm(instance=product)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
            
                form.save()
                url = reverse("one_product.index", args=[product.id])

                return redirect(url)

        return render(request, 'products/edit_product.html', {'form': form, 'product': product, })
    else:
        return redirect("products.index")

# Let's Write Views in a new way, class based views

#Version 2 of 