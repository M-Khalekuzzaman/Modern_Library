from django.urls import path
from .import views

urlpatterns = [
    path('show_book/',views.show_book, name = 'show_book'), 
    path('books/delete_book/<int:book_id>',views.delete_book, name = 'delete_book'),
    path('show_book/details_book/<int:book_id>',views.details_book, name = "details_book"),
]
