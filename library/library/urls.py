
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('bookservice_app.urls')),
    path('member/',include('memberservice_app.urls')),
    path('borrowing/',include('borrowingservice_app.urls')),
    path('librarian/',include('librarian_dashboard.urls'), name='librarian_dashboard'),
]
