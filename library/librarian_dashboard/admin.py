from django.contrib import admin
from .models import Book, Member, Borrowing

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies')
    search_fields = ('title', 'author', 'isbn')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'membership_date')
    search_fields = ('first_name', 'last_name', 'email')
    

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('member', 'book', 'borrow_date', 'due_date', 'return_date')
    search_fields = ('member__first_name', 'member__last_name', 'book__title')
  