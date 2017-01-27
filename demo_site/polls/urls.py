from django.config.urls import urls

from . import views

urlpattern = [
			url(r'^$',views.index,name = 'index')
]