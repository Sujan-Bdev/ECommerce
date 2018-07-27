from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory

from backend.models import Customer, Book, Author, BookLinkAuthor, Category

from django.contrib.auth.models import User


class BookCreateForm(forms.ModelForm):
    class Meta:
        model=Book
        exclude=('slug',)





class AuthorCreateForm(forms.Form):

    def __init__(self,*args, **kwargs):
        no=kwargs.pop("no")
        super(AuthorCreateForm, self).__init__(*args, **kwargs)
        for i in range(0,no):
            self.fields["author_name %d" % (i+1)] = forms.CharField()
            self.fields["email_for %d" % (i+1)] = forms.CharField()

    def save(self,book):
        for i in range(0,book.no_authors):
            name=self.cleaned_data["author_name %d" %i]
            email=self.cleaned_data["email_name %d" %i]
            author=Author.objects.create(name=name,email=email)
            BookLinkAuthor.objects.create(book=book,author=author)





