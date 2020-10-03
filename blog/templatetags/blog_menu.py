from django import template

from blog.models import Category, Tags

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}


@register.inclusion_tag('blog/sidebar_tags_tpl.html')
def show_tags():
    tags = Tags.objects.all()
    return {'tags': tags}
