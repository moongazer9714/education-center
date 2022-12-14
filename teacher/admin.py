from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Teacher


class TeacherAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm
    list_display = ('id', 'full_name', 'get_photo',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'


admin.site.register(Teacher, TeacherAdmin)
