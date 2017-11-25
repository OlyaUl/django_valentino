from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from redis import Redis
# from .models import Product


def index(request):
    return render(request, 'valentino/index.html', {})


