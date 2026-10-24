from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Обратная связь: {name}, тел. {phone}: {message}")
        return HttpResponse(f"Привет, {name}, мы скоро свяжемся с Вами!")
    return render(request, "contacts.html")
