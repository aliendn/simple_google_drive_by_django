from django.urls import path
from .views import BookListView, AuthorDetailView

urlpatterns = [
    path('publishers/', BookListView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail')
]