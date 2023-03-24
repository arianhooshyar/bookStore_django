from django.shortcuts import render
from .models import Book
from django.views import generic


class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book_list_view.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'price']
    template_name = 'book/book_create.html'
