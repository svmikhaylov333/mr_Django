from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact


def home(request):
    latest_product_list = Product.objects.order_by('-created_at')[:5]
    print("Последние 5 созданных продуктов")
    for product in latest_product_list:
        print(product.name)
    context = {"latest_product_list": latest_product_list}
    return render(request, "home.html", context)


def contacts(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Обратная связь: {name}, тел. {phone}: {message}")
        Contact.objects.create(name=name, phone=phone, message=message)


        return HttpResponse(f"Спасибо, {name}! Мы скоро свяжемся с Вами!")
    return render(request, "contacts.html")
