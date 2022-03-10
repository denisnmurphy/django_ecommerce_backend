from unicodedata import decimal
from webbrowser import get
from django.forms import DecimalField
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from store.models import Collection, OrderItem, Product, Order
from tags.models import TaggedItem



def say_hello(request):
    with connection.cursor() as cursor:
        cursor.execute()

    return render(request, 'hello.html', {'name': 'Mosh'})
