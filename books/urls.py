from django.urls import path
from .views import book_detail, update_rating

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book/<int:book_id>/rate/', update_rating, name='update_rating'),
]
