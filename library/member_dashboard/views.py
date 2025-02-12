from django.shortcuts import render
from datetime import date
from borrowingservice_app.models import Borrowing
from bookservice_app.models import Book
from django.contrib.auth.decorators import login_required

@login_required
def member_dashboard(request):
    member = request.user
    borrowed_books = Borrowing.objects.filter(member=member, return_date__isnull=True)
    borrowing_history = Borrowing.objects.filter(member=member)
    overdue_books = borrowed_books.filter(due_date__lt=date.today())
    context = {
        'borrowed_books': borrowed_books,
        'borrowing_history': borrowing_history,
        'overdue_books': overdue_books,
    }
    return render(request, 'member_dashboard.html', context)
