from rest_framework import viewsets
from datetime import date
from .models import Book, Member, Borrowing
from .serializers import BookSerializer, MemberSerializer, BorrowingSerializer
from django.shortcuts import render
from django.db.models import Count

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer

def librarian_dashboard(request):
    total_books = Book.objects.count()
    total_members = Member.objects.count()
    books_borrowed = Borrowing.objects.filter(return_date__isnull=True).count()
    overdue_books = Borrowing.objects.filter(return_date__isnull=True, due_date__lt=date.today()).count()
    popular_books = Book.objects.annotate(borrow_count=Count('borrowing')).order_by('-borrow_count')[:5]
    context = {
        'total_books': total_books,
        'total_members': total_members,
        'books_borrowed': books_borrowed,
        'overdue_books': overdue_books,
        'popular_books': popular_books,
    }
    return render(request, 'librarian_dashboard.html', context)
