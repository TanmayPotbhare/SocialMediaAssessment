from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('librarian_page/', views.librarian_page, name='librarian_page'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit-book/<int:id>/', views.update_book, name='update_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),
    path('get_book/<int:book_id>/', views.get_book_api, name='get_book_api'),
    path('search-api/', views.search_api_page, name='search_api_page'),
    path('search_books_api/', views.search_books_api, name='search_books_api'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
