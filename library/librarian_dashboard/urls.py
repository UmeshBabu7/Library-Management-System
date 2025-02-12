from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, BorrowingViewSet, librarian_dashboard

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrowings', BorrowingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('librarian/dashboard/', librarian_dashboard, name='librarian_dashboard'),
]
