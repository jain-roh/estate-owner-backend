from django.contrib.auth.models import User
from .models import Property
import django_filters

class PropertyFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Property
        fields = {
            'price':['lte','gte'],
            'address1':['exact'],
            'address2':['exact'],
            'city':['exact'],
            'state':['exact'],
            'beds':['gte'],
            'bath':['gte'],
            'propertytype':['exact']
        }