from django.urls import path

from . import views

app_name = 'recorder'
urlpatterns = [
    path('', views.form, name='form'),
    path('complete', views.complete, name='complete'),
]
