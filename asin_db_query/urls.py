from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin


from .views import get_asin


urlpatterns = [
    url(r'', get_asin, name='get_asin'),

]