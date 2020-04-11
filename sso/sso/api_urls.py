from django.urls import path

from . import views

app_name = 'sso_api'

urlpatterns = [
    path('user/', views.user),
]
