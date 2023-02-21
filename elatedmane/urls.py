# pylint: disable=missing-module-docstring
from django.conf.urls import include
from django.urls import path

from rest_framework import routers
from maneapi.views import register_user, login_user
from maneapi.views import StylistView, CustomerView

# pylint: disable=invalid-name
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'stylists', StylistView, 'stylist')
router.register(r'customers', CustomerView, 'customer')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
]
