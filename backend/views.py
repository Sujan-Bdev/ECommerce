# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # boards = Board.objects.all()
    return render(request, 'home.html')


def sample(request):
    # boards = Board.objects.all()
    return render(request, 'sample.html')


def index(request):
    return HttpResponse("Hello, world. I am creating the hamro pustak bhandar.")

class CustomerSignUpView(FormView):
    template_name = 'registration/signup_form.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super().form_valid(form)


class StaffSignUpView(FormView):
    template_name = 'registration/signup_form.html'
    form_class = StaffCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
            user = form.save()
            user.save()
         
            
