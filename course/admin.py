from django.contrib import admin
from .models import Course, Category, Tag

from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'get_photo',)
    list_display_links = ('id', 'title')
    readonly_fields = ('created_at', 'get_photo')
    search_fields = ('title',)
    list_filter = ('category__title', 'tag', 'id')
    date_hierarchy = 'created_at'

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ['title', ]
    list_display_links = ('title', 'id')
    list_per_page = 50
    search_help_text = 'search on here'


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title', ]
    list_filter = ('id', 'title')
    list_display_links = ('title', 'id')
    search_help_text = 'search on here'


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
