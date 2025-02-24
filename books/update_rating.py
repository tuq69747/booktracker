from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book

def update_rating(request, book_id):
    if request.method == 'POST':
        rating = int(request.POST.get('rating', 0))
        book = get_object_or_404(Book, pk=book_id)
        book.rating = rating
        book.save()
        return JsonResponse({'success': True, 'rating': rating})
    return JsonResponse({'success': False})
