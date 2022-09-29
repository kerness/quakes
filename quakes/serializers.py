from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Quake


class QuakeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Quake
        geo_field = 'geom'
        fields = '__all__'
