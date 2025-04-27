# lostitems/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Count
from datetime import datetime, timedelta
from .models import LostItem
from .forms import LostItemForm

# View para a página inicial (landing page)
def home_view(request):
    # Obtém dados para estatísticas
    total_items = LostItem.objects.count()
    
    # Itens da última semana
    one_week_ago = datetime.now() - timedelta(days=7)
    recent_items = LostItem.objects.filter(created_at__gte=one_week_ago).count()
    
    # Locais distintos
    total_locations = LostItem.objects.values('lost_location').distinct().count()
    
    # Itens recentes para exibição (últimos 3)
    recent_items_list = LostItem.objects.all().order_by('-created_at')[:3]
    
    context = {
        'total_items': total_items,
        'recent_items': recent_items,
        'total_locations': total_locations,
        'recent_items_list': recent_items_list,
    }
    
    return render(request, 'home.html', context)

# View para listar todos os itens perdidos (com filtro de busca)
class LostItemListView(ListView):
    model = LostItem
    template_name = 'list.html'
    context_object_name = 'lost_items'
    paginate_by = 9  # Paginação com 9 itens por página
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtros de busca
        query = self.request.GET.get('q', '')
        location = self.request.GET.get('location', '')
        
        if query:
            queryset = queryset.filter(name__icontains=query)
        
        if location:
            queryset = queryset.filter(lost_location__icontains=location)
            
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['location'] = self.request.GET.get('location', '')
        
        # Lista de locais para o dropdown de filtro
        context['locations'] = LostItem.objects.values_list('lost_location', flat=True).distinct()
        
        return context

# View para detalhar um item perdido específico
class LostItemDetailView(DetailView):
    model = LostItem
    template_name = 'detail.html'  # Mantendo 'detail.html' conforme seu projeto
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