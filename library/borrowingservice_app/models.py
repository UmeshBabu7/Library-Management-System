from django.db import models

# Create your models here.

from memberservice_app.models import Member
from bookservice_app.models import Book

class Borrowing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.member} borrowed {self.book}"
