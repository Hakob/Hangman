from django.urls import path
from .views import create_user, log_in, log_out

urlpatterns = [
    path(route='create/',
         view=create_user,
         name='create'),

    path(route='login/',
         view=log_in,
         name='login'),

    path(route='logout/',
         view=log_out,
         name='logout'),
]
