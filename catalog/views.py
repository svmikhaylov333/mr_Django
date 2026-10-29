from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Contact, Product


def products_list(request):
    # latest_product_list = Product.objects.order_by("-created_at")[:5]
    # print("Последние 5 созданных продуктов")
    latest_product_list = Product.objects.all()
    for product in latest_product_list:
        print(product.name)
    context = {"latest_products_list": latest_product_list}
    return render(request, "products_list.html", context)


def contacts(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Обратная связь: {name}, тел. {phone}: {message}")

        if name and phone and message:
            Contact.objects.create(name=name, phone=phone, message=message)
            return HttpResponse(f"Спасибо, {name}! Мы скоро свяжемся с Вами!")
        else:
            return HttpResponse("Ошибка: заполните все поля!")
    return render(request, "contacts.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
