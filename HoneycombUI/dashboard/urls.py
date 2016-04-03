from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'dashboard.views.index', name='index'),
    url(r'^index/$', 'WebApp.views.index', name='index'),

]