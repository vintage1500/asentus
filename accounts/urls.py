from django.urls import path
from . import views


urlpatterns = [
    path('', views.account_view, name='account')
]