from django.shortcuts import render, redirect ,reverse
# from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login

from django.contrib.auth.models import User
from accounts.forms import RegistrationForm

# Create your views here.

@login_required()
def profile(request):
    print("User.id",request.user.id)
    url = reverse("products.index")
    return redirect(url)


class AccountsDetailView(DetailView):
    model = User
    template_name = 'accounts/accounts_detail.html'


class AccountCreateView(CreateView):
    model = User
    template_name = 'accounts/create.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')  # Use reverse_lazy for dynamic URL resolution

    # Optional: Log in user right after registration
    def form_valid(self, form):
        response = super().form_valid(form)
        # Auto-login after registration
        user = form.save()
        login(self.request, user)
        return redirect("products.index")

