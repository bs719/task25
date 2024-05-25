from django.urls import path
from . import views

urlpatterns = [
    path('my-url/', views.my_view, name='my-view'),
]
