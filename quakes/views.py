from quakes.models import Quake
from quakes.serializers import QuakeSerializer
from rest_framework import generics
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
import logging
from django_filters.rest_framework import DjangoFilterBackend


# TODO: zwracanie z konkretnego przedziału dat
# Może zrobić tak, żeby USGS, GRSS miały całkowicie inne endpointy - quakes/usgs, quakes/grss

class QuakeDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Return a single Quake by PK """
    queryset = Quake.objects.all()
    serializer_class = QuakeSerializer

class QuakeList(generics.ListAPIView):
    """View to list all quakes or quakes by specified vendor"""
    serializer_class = QuakeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vendor']
    logger = logging.getLogger(__name__)
    

    def get_queryset(self):
        """Pass vendor to get quakes provided by this vendor"""
        queryset = Quake.objects.all()
        vendor_name = self.request.query_params.get('vendor')
        lat = self.request.query_params.get('lat')
        lng = self.request.query_params.get('lng')
        radius = self.request.query_params.get('radius')

        self.logger.debug(f'Given parameters: lat: {lat}, lng: {lng}, radius: {radius}')


        if lat and lng and radius is not None:
            point = Point(float(lat), float(lng), srid=4326)
            queryset = Quake.objects.filter(geom__distance_lte=(point, D(km=float(radius))))

        return queryset



