from django.conf.urls import url
from valentino import views


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]