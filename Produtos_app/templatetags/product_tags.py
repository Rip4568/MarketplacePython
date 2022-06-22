from django import template
from django.utils import timezone


register = template.Library()

@register.filter()
def remainder(n):
    return n % 3

@register.tag()
def calcular_idade(idade):
    ano_atual = timezone.now().year
    return ano_atual - idade
