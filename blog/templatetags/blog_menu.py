from django import template

from blog.models import Category, Tags, Posts

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}


@register.inclusion_tag('blog/sidebar_recent_tpl.html')
def show_recent(cnt=3):
    recent = Posts.objects.order_by('-created_at')[:cnt]
    return {'recent': recent}


@register.inclusion_tag('blog/sidebar_popular_tpl.html')
def show_popular(cnt=3):
    popular = Posts.objects.order_by('-views')[:cnt]
    return {'popular': popular}


@register.inclusion_tag('blog/sidebar_tags_tpl.html')
def show_tags():
    tags = Tags.objects.all()
    return {'tags': tags}


@register.inclusion_tag('blog/serch_tags_tpl.html')
def show_search():
    return None
