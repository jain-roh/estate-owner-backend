from django.contrib.auth.models import User
from .models import Property
import django_filters

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ['address1','address2','city','state', 'price','beds','bath','size','description','propertytype' ]