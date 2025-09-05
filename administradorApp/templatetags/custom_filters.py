import json
from django import template

register = template.Library()

@register.filter
def map(value, arg):
    """Aplica una función map para extraer una clave específica de un diccionario"""
    return [getattr(v, arg, None) if hasattr(v, arg) else v.get(arg, None) for v in value]

@register.filter
def json_encode(value):
    """Convierte el valor en formato JSON"""
    return json.dumps(value)
