from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from .models import *


class LessonAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Lesson
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    category_landing = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Category
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    prepopulated_fields = {"slug": ("title",)}
    form = LessonAdminForm
    save_as = True


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = CategoryAdminForm
    save_as = True


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)
