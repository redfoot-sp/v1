from django.contrib import admin
from .models import LawFile

#admin.site.register(LawFile)
@admin.register(LawFile)
class LawFileAdmin(admin.ModelAdmin):
    fields = ('type_law', 'number_law', 'date_publish', 'name_law', 'desc_law', 'file_law',)
    list_display = ('type_law', 'number_law', 'name_law', 'file_law',)
    list_display_links = None
    list_editable = ('type_law', 'number_law', 'name_law')