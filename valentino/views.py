from django.shortcuts import render, redirect
from redis import Redis
from django.views.generic import TemplateView
from .models import Product


class SpiderView(TemplateView):
    template_name = "valentino/index.html"

    def post(self, request, *args, **kwargs):
        url1 = request.POST.get('url')
        spider = request.POST.get('spider')
        redis = Redis()
        redis.lpush('{0}:start_urls'.format(spider), url1)
        return redirect('index')


def all_data(request):
    all = Product.objects.all()
    return render(request, 'valentino/data.html', {'products': all})


# def index(request):
#     return render(request, 'valentino/index.html', {})


