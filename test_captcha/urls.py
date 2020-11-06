from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.show_form, name='show_form'),
    path('log_user_image_click', views.log_user_image_click, name='log_user_image_click'),
]