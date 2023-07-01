from django.urls import path
from .views import *


urlpatterns = [
    path('', gettybal, name="gettybalance"),
    path('services/', services, name="services"),
    path('apply-now/', apply_now, name="apply-now"),
]