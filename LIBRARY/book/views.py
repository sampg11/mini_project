from urllib import response
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Exists, OuterRef
from django.shortcuts import render, get_object_or_404, redirect
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

    def get_queryset(self):
        user = self.request.user
        fav_subquery = Book.favorited_by.through.objects.filter(
            book_id=OuterRef('pk'), user_id=user.pk
        )
        return Book.objects.all().annotate(is_favorited=Exists(fav_subquery))


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
    paginate_by = 10


    def get_queryset(self):
        from django.db.models import Exists, OuterRef
        query = self.request.GET.get('q', '').strip()
        user = self.request.user
        fav_subquery = Book.favorited_by.through.objects.filter(
            book_id=OuterRef('pk'), user_id=user.pk
        )
        queryset = Book.objects.all().prefetch_related('authors').annotate(is_favorited=Exists(fav_subquery))
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(authors__first_name__icontains=query)|
                Q(authors__last_name__icontains=query)).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
class FavoriteListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'home/favorites.html'
    context_object_name = 'books'
    paginate_by = 10
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return self.request.user.favorite_books.all().prefetch_related('authors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for book in context['books']:
            book.is_favorited = True
        return context


@login_required
def toggle_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.favorited_by.filter(pk=request.user.pk).exists():
        book.favorited_by.remove(request.user)
    else:
        book.favorited_by.add(request.user)

    next_url = request.POST.get('next') or request.GET.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('book_list')

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('book_list'))