# lostitems/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import LostItem
from .forms import LostItemForm

# View para listar todos os itens perdidos
class LostItemListView(ListView):
    model = LostItem
    template_name = 'list.html'
    context_object_name = 'lost_items'
    paginate_by = 9  # Paginação com 9 itens por página

# View para detalhar um item perdido específico
class LostItemDetailView(DetailView):
    model = LostItem
    template_name = 'detail.html'
    context_object_name = 'item'

# View para criar um novo item perdido
class LostItemCreateView(CreateView):
    model = LostItem
    form_class = LostItemForm
    template_name = 'register.html'
    success_url = reverse_lazy('lost_item_list')

    def form_valid(self, form):
        # Podemos adicionar lógica adicional antes de salvar se necessário
        return super().form_valid(form)

# View para a página inicial (redireciona para a listagem)
def home_view(request):
    return redirect('lost_item_list')