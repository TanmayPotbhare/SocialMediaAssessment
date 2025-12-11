import json

import requests
from django.http import JsonResponse
from .models import Book
from .forms import BookForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count


# Homepage
def homepage(request):
    return render(request, 'products/home.html')


# Librarian dashboard showing all books
def librarian_page(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'products/librarian_page.html', {'books': books, 'form': form})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('librarian_page')
    return redirect('librarian_page')


def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('librarian_page')
    else:
        form = BookForm(instance=book)

    return render(request, "update_book.html", {"form": form})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("librarian_page")


def get_book_api(request, book_id):
    """AJAX – Return book details in JSON"""
    book = get_object_or_404(Book, id=book_id)
    data = {
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "published_year": book.published_year,
        "pages": book.pages,
        "isbn": book.isbn,
        "genre": book.genre,
    }
    return JsonResponse(data)


def search_api_page(request):
    return render(request, "products/search_api.html")


def search_books_api(request):
    """
    AJAX view to fetch data from Google Books API.
    Supports:
        intitle:
        inauthor:
        isbn:
        inpublisher:
        OR plain query
    """
    query = request.GET.get("query")

    if not query:
        return JsonResponse({"error": "Query is required"}, status=400)

    google_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    try:
        response = requests.get(google_url, timeout=5)
        data = response.json()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def dashboard(request):
    # Books count per author
    author_data = Book.objects.values('author').annotate(total=Count('id')).order_by('-total')
    author_labels = [item['author'] for item in author_data]
    author_counts = [item['total'] for item in author_data]

    # Books count per year
    year_data = Book.objects.values('published_year').annotate(total=Count('id')).order_by('published_year')
    year_labels = [item['published_year'] for item in year_data]
    year_counts = [item['total'] for item in year_data]

    # Books count per genre
    genre_data = Book.objects.values('genre').annotate(total=Count('id')).order_by('-total')
    genre_labels = [item['genre'] for item in genre_data]
    genre_counts = [item['total'] for item in genre_data]

    context = {
        'total_books': Book.objects.count(),
        'author_labels': json.dumps(author_labels),
        'author_counts': json.dumps(author_counts),
        'year_labels': json.dumps(year_labels),
        'year_counts': json.dumps(year_counts),
        'genre_labels': json.dumps(genre_labels),
        'genre_counts': json.dumps(genre_counts),
    }

    return render(request, 'products/dashboard.html', context)