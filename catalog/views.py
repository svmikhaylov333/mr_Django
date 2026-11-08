from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Contact, Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductContactView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Обратная связь: {name}, тел. {phone}: {message}")
        if name and phone and message:
            Contact.objects.create(name=name, phone=phone, message=message)
            return HttpResponse(f"Спасибо, {name}! Мы скоро свяжемся с Вами!")

        return HttpResponse("Ошибка: заполните все поля!")
