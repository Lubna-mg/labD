﻿from django.shortcuts import render


def index(request):
    return render(request, 'bookmodule/index.html')


def viewbook(request, bookId):
  
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
   
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2
    
    
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)
