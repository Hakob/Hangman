from django.urls import path
from .views import sign_up, log_in, log_out

urlpatterns = [
    path(route='signup/',
         view=sign_up,
         name='signup'),

    path(route='login/',
         view=log_in,
         name='login'),

    path(route='logout/',
         view=log_out,
         name='logout'),
]
