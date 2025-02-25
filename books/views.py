from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Book

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def update_rating(request, book_id):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        rating = int(data.get('rating', 0))
        book = get_object_or_404(Book, pk=book_id)
        book.rating = rating
        book.save()
        return JsonResponse({'success': True, 'rating': rating})
    return JsonResponse({'success': False})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
