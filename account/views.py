from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from . import forms


class CustomerSignUpView(FormView):
    template_name = 'registration/signup_form.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super().form_valid(form)


class StaffSignUpView(FormView):
    template_name = 'registration/signup_form_admin.html'
    form_class = forms.StaffCreateForm
    success_url = reverse_lazy('signup_admin')

    def form_valid(self, form):
            user = form.save()
            user.save()
            return super().form_valid(form)



# Create your views here.
