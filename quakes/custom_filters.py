from django_filters import rest_framework as filters
from quakes.models import Quake

class QuakesFilter(filters.FilterSet):
    mag = filters.RangeFilter()
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Quake
        fields = ["mag", "vendor", "date"]