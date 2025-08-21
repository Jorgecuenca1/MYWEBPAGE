from django import template
from datetime import datetime

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """Divide una cadena por el delimitador especificado"""
    if value:
        return value.split(delimiter)
    return []

@register.filter
def strip(value):
    """Elimina espacios en blanco al inicio y final"""
    if value:
        return value.strip()
    return value

@register.simple_tag
def current_year():
    """Retorna el año actual"""
    return datetime.now().year

@register.filter
def percentage_width(value):
    """Convierte un porcentaje a un ancho CSS"""
    try:
        return f"{int(value)}%"
    except (ValueError, TypeError):
        return "0%"
