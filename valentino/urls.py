from django.conf.urls import url
from valentino import views
from . import views


urlpatterns = [
    # url(r'^index/$', views.index, name='index'),
    url(r'^$', views.SpiderView.as_view(), name='index'),
]