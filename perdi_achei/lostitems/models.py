# lostitems/models.py

from django.db import models
from django.urls import reverse

class LostItem(models.Model):
    name = models.CharField('Nome do Item', max_length=100)
    description = models.TextField('Descrição')
    image = models.ImageField('Imagem', upload_to='items/')
    lost_location = models.CharField('Local Perdido', max_length=100)
    contact_info = models.CharField('Informações de Contato', max_length=100)
    additional_comments = models.TextField('Comentários Adicionais', blank=True, null=True)
    created_at = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    class Meta:
        verbose_name = 'Item Perdido'
        verbose_name_plural = 'Itens Perdidos'
        ordering = ['-created_at']  # Ordenar por data de criação (mais recente primeiro)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lost_item_detail', args=[str(self.id)])

    def is_whatsapp_contact(self):
        # Verifica se o contato é um número de telefone internacional
        # Simplificado: procura +número
        import re
        return bool(re.match(r'^\+\d+', self.contact_info))

    def get_whatsapp_url(self):
        if not self.is_whatsapp_contact():
            return None
        # Remove espaços e caracteres especiais
        clean_number = ''.join(char for char in self.contact_info if char.isdigit() or char == '+')
        message = "Olá, encontrei um item perdido. Gostaria de saber mais sobre o item que você cadastrou."
        import urllib.parse
        encoded_message = urllib.parse.quote(message)
        return f"https://wa.me/{clean_number}?text={encoded_message}"