from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory

from backend.models import Customer, Book, Author, BookLinkAuthor

from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    location = forms.CharField()
    contact = forms.CharField()

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            first_name=self.cleaned_data['first_name'],
                                            last_name=self.cleaned_data['last_name'],
                                            password=self.cleaned_data['password'],
                                            email=self.cleaned_data['email'],
                                            )
        m1 = Customer.objects.create(user=new_user, location=self.cleaned_data.get('location'),
                                     contact=self.cleaned_data.get('contact'))
        m1.save()
        return new_user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


class StaffCreateForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text="Confirm Password")
    location = forms.CharField()
    contact = forms.CharField()

    def clean(self):
        cleaned_data = super(StaffCreateForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        password_validation.validate_password(password=password, user=username)
        if password != password2:
            raise forms.ValidationError("The two password are not same")
        return cleaned_data

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            first_name=self.cleaned_data['first_name'],
                                            last_name=self.cleaned_data['last_name'],
                                            password=self.cleaned_data['password'],
                                            email=self.cleaned_data['email'],
                                            is_staff=self.cleaned_data['is_staff'],
                                            )
        m1 = Customer.objects.create(user=new_user, location=self.cleaned_data.get('location'),
                                     contact=self.cleaned_data.get('contact'))
        m1.save()
        return new_user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
