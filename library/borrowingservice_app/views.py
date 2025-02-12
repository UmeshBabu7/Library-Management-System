from django.shortcuts import render
from rest_framework import viewsets
from .models import Borrowing
from .serializers import BorrowingSerializer

# Create your views here.

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
