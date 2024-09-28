from django.shortcuts import render

from .models import Category, Phone


def home_page(request):
    phones = Phone.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        "index.html",
        context={
            "phones": phones,
            "categories": categories,
        },
    )
