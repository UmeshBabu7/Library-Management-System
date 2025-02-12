from rest_framework import generics
from bookservice_app.models import Book
from memberservice_app.models import Member
from bookservice_app.serializers import BookSerializer
from memberservice_app.serializers import MemberSerializer
from rest_framework.response import Response

class SearchView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        books = Book.objects.filter(title__icontains=query)
        members = Member.objects.filter(first_name__icontains=query) | Member.objects.filter(last_name__icontains=query)
        book_serializer = BookSerializer(books, many=True)
        member_serializer = MemberSerializer(members, many=True)
        return Response({
            'books': book_serializer.data,
            'members': member_serializer.data
        })
