from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<connection_name>.+)/$', views.detail, name='detail'),
]
