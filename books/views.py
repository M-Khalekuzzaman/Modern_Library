from django.shortcuts import render
from .models import StoreBookModel

def show_book(request):
    books = StoreBookModel.objects.all()
    return render(request,'show_book.html',{'books':books})

def delete_book(request,book_id):
    book = StoreBookModel.objects.get(book_id = book_id).delete()
    
def details_book(request,book_id):
    book = StoreBookModel.objects.get(book_id = book_id)
    return render(request,'details_book.html',{'book':book})
