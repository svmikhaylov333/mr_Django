from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .forms import ProductForm
from .models import Contact, Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})

class ProductContactView(CreateView):
    model = Contact
    fields = ["name", "phone", "message"]
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:contacts")

    def form_valid(self, form):
        print(f"Обратная связь: {form.cleaned_data['name']}, тел. {form.cleaned_data['phone']}")
        return super().form_valid(form)


