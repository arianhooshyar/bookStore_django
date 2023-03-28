from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, BookAddCommentView

urlpatterns = [
    path('', BookListView.as_view(), name="Book_list_view"),
    path('<int:pk>/', BookDetailView.as_view(), name='Book_detail_view'),
    path('create/', BookCreateView.as_view(), name='Book_create_View'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='Book_update_view'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='Book_delete_view'),
    path('<int:pk>/comment/', BookAddCommentView.as_view(), name='Book_comment_view'),
    # path('<int:pk>/admin/book/comment/add/', BookAddCommentView.as_view(), name='Book_comment_view')

]
