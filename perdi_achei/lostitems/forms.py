# lostitems/forms.py

from django import forms
from .models import LostItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['name', 'description', 'image', 'lost_location', 'contact_info', 'additional_comments']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-md', 'rows': 3}),
            'lost_location': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md'}),
            'contact_info': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md', 'placeholder': '+5511999999999'}),
            'additional_comments': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-md', 'rows': 2}),
        }
        labels = {
            'name': 'Nome do Item',
            'description': 'Descrição',
            'image': 'Imagem',
            'lost_location': 'Local onde foi perdido',
            'contact_info': 'Informações de contato (preferência telefone com +55)',
            'additional_comments': 'Comentários adicionais (opcional)',
        }
        help_texts = {
            'contact_info': 'Para habilitar o botão de WhatsApp, utilize o formato internacional: +5511999999999'
        }