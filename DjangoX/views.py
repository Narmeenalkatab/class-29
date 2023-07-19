from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import DjangoX


class DjangoXListView(ListView):
    template_name = "DjangoX/DjangoX-list.html"
    model = DjangoX


class DjangoXDetailView(DetailView):
    template_name = "DjangoX/DjangoX-detail.html"
    model = DjangoX


class DjangoXCreateView(CreateView):
    template_name = "DjangoX/DjangoX-create.html"
    model = DjangoX
    fields = ['name', 'desc', 'purcheser']


class DjangoXUpdateView(UpdateView):
    template_name = "DjangoX/DjangoX-update.html"
    model = DjangoX
    fields = ['name', 'desc', 'purcheser']


class DjangoXDeleteView(DeleteView):
    template_name = "DjangoX/DjangoX-delete.html"
    model = DjangoX
    success_url = reverse_lazy("DjangoX_list")