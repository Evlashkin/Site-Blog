from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from blog.models import Posts, Category, Tags


class PostsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'


class PostsAdmin(admin.ModelAdmin):
    form = PostsAdminForm
    save_on_top = True
    save_as = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created_at', 'author', 'get_photo', 'category', 'views')
    list_display_links = ('title', 'created_at', 'author', 'category')
    list_filter = ['created_at', 'category', 'tags']
    search_fields = ('title', 'content')
    readonly_fields = ['views', 'created_at', 'get_photo']
    fields = ['title', 'slug', 'content', 'author', 'photo', 'get_photo', 'views', 'category', 'tags', 'created_at']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="60">')
        return 'отсутствует изображение'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Posts, PostsAdmin)
