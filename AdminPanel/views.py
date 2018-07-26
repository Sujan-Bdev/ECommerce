from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from backend.models import Book
from . import forms


def admin_panel(request):

    no_books=Book.objects.all().count()
    no_users=User.objects.all().count()
    no_staff=User.objects.filter(is_staff=True).count()
    return render(request,'Admin Panel/index.html',{'no_books':no_books,'no_users':no_users,'no_staff':no_staff})

def AddBook(request):
    if request.method=="POST":
        form = forms.BookCreateForm(request.POST)

        if form.is_valid():
            book=form.save(commit=False)
            book.save()
            form.save_m2m()
            return redirect('add_book_author',pk=book.id)
    else:
        form=forms.BookCreateForm()

    return render(request, 'Admin Panel/book_form.html', {"form":form})

def AddAuthor(request,pk):
    book=get_object_or_404(Book,pk=pk)
    if request.method=="POST":
        form = forms.AuthorCreateForm(request.POST,no=book.no_authors)
        if form.is_valid():
            print("yes from is valid")
            form.save(book)

    else:
        form=forms.AuthorCreateForm(no=book.no_authors)

    return render(request, 'Admin Panel/author_form.html', {"form":form})
