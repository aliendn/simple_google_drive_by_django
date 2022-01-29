from django.views.generic import ListView
from t.models import Publisher, Book
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Author
from django.utils import timezone
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# class PublisherListView(ListView):
#     model = Publisher
#     context_object_name = 'publishers'


class BookListView(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


class AuthorDetailView(DetailView):

    queryset = Author.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')