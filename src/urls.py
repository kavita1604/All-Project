from django.conf import urls

from . import views

urlpatterns = [
    urls.url(r'^$', views.index,name='index'),
    urls.url(r'hi', views.hi,name='hi')
]
