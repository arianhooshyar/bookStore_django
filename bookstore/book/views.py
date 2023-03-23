from django.shortcuts import render
from .models import Book
from django.views import generic


class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book_list_view.html'
    context_object_name = 'books'
