from django.contrib.auth.models import User
from .models import Property
import django_filters

class PropertyFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    # address1=django_filters.CharFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    address1=django_filters.CharFilter(lookup_expr='icontains')
    manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Property
        fields = {
            'user':['exact'],
            'price':['lte','gte'],
            'address1':['contains'],
            'address2':['exact'],
            'city':['exact'],
            'state':['exact'],
            'beds':['gte'],
            'bath':['gte'],
            'propertytype':['exact']
        }