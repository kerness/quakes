from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Quake


class QuakeSerializer(GeoFeatureModelSerializer):
    """  class to serialize quakes location as GeoJSON data. """
    class Meta:
        model = Quake
        geo_field = 'geom'
        fields = '__all__'



