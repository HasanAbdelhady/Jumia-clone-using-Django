from django.shortcuts import render, get_object_or_404, reverse, redirect
from category.models import Category
from category.forms import Category_form
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def is_superuser(user):
    return user.is_superuser
 
def show_categories(request):
    categories = Category.objects.all().order_by('id')
    return render(request, "category/index.html", {"categories":categories})

def show_category(request, id):

    category = get_object_or_404(Category, id=id)
    return render(request, "category/category.html", {"category":category})

def create_new_category(request):
    if request.method == "POST":
        form = Category_form(request.POST)
        if form.is_valid():
            category = form.save()
            url = reverse("category.show", args=[category.id])
            return redirect(url)
    else:
        form = Category_form()  # Show an empty form on GET request

    return render(request, 'category/add_category.html', {"form": form})

@method_decorator([login_required, user_passes_test(is_superuser, login_url=reverse_lazy('categories.show'))], name='dispatch')
class Create_Category(CreateView):
    model = Category
    form_class = Category_form
    template_name = 'category/add_category.html'

    def form_valid(self, form):
        if form.is_valid():
            category = form.save(commit=False)
            category.user = self.request.user 
            category.save()
            return redirect('categories.show')
