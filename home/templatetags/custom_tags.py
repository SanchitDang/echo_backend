import urllib.request
from django import template

register = template.Library()

@register.filter
def is_url_valid(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.status == 200
    except:
        return False
