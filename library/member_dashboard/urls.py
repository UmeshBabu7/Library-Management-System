from django.urls import path
from .views import member_dashboard

urlpatterns = [
    path('memberdashboard/', member_dashboard, name='member_dashboard'),
]