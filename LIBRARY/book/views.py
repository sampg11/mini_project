from urllib import response

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm, BookForm
from .models import Book


# Create your views here.


def homepage(request):
    return render(request, "home/home_page.html")



class RegisterPageView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'home/register.html'
    success_url =reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request,self.object)
        return response

@login_required
def welcom_view(request):
    return render(request, "home/welcom.html")

class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book
    paginate_by = 8
    template_name = 'home/book_list.html'


class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book
    template_name = 'home/detail_view.html'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('authors')

class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'home/book_form.html'
    success_url = reverse_lazy('book_list')
    login_url = reverse_lazy('login')



class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'home/book_form.html'
    success_url = reverse_lazy('book_list')
    login_url = reverse_lazy('login')

class BookSearchView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'home/book_search.html'
    context_object_name = 'books'
    paginate_by = 12


    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        queryset = Book.objects.all().prefetch_related('authors')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(authors__first_name__icontains=query)|
                Q(authors__last_name__icontains=query)).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('book_list'))