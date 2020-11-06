from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.render_puzzle, name='render_puzzle'),
    path('log_user_image_click', views.log_user_image_click, name='log_user_image_click'),
]
