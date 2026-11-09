from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy

from .models import Contact, Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductContactView(CreateView):
    model = Contact
    fields = ["name", "phone", "message"]
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:contacts")

    def form_valid(self, form):
        print(f"Обратная связь: {form.cleaned_data['name']}, тел. {form.cleaned_data['phone']}")
        return super().form_valid(form)
