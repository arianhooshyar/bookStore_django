from django.urls import path
from .views import BookListView
urlpatterns = [
    path('', BookListView.as_view(), name="Book_list_view"),
]