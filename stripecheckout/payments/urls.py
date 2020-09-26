from django.contrib import admin
from django.urls import path, include
from .views import HomePage, get_publishable_key, create_checkout, SuccessPage, CancelPage

urlpatterns = [
    path('', HomePage.as_view(), name='Home'),
    path('config/', get_publishable_key, name='publishKey'),
    path('create_session/', create_checkout, name='checkout'),
    path('cancelled/', CancelPage.as_view(), name='Home'),
    path('success/', SuccessPage.as_view(), name='Success')
]