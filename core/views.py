from django.shortcuts import render
from .models import Item

def item_list(request):
    context = {
        'items': Item.objects.all()
    }

    return render(request, "home_page.html", context)

# Create your views here.
