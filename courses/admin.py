from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Course , Comment
from django.db import models

class CourseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Course, CourseAdmin)

admin.site.register(Comment)