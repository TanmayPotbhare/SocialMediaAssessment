from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'description', 'published_year', 'pages', 'genre']
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN / Barcode'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Book Description'}),
            'published_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Published Year'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Pages'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
        }
