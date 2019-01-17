from .models import LawFile
import django_filters


class LawFilter(django_filters.FilterSet):
    class Meta:
        model = LawFile
        fields = ['type_law', 'number_law', 'desc_law']
