from django.urls import include, path
from . import views

urlpatterns = [
    path('captcha', views.show_form, name='show_form'),
    path('index', views.index, name='index'),
    path('log_user_image_click', views.log_user_image_click, name='log_user_image_click'),
    path('log_index_input', views.log_index_input, name='log_index_input'),
]