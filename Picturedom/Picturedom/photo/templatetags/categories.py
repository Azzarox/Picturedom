from django import template

from Picturedom.photo.models import Category

register = template.Library()


@register.inclusion_tag('components/category_navbar.html')
def categories():
    categories = Category.objects.order_by('title')
    return {
        'categories': categories
    }
