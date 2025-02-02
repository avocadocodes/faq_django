from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django.db import models

class FAQAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
    list_display = ['question', 'language']
    search_fields = ['question']

admin.site.register(FAQ, FAQAdmin)
