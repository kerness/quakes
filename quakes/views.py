from argparse import Action
from rest_framework import viewsets, status
from .models import Quake
from .serializers import QuakeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

class QuakeViewSet(viewsets.ModelViewSet):
    queryset = Quake.objects.all()
    serializer_class = QuakeSerializer
    

    # @action(detail=True)
    # def quakes_by_vendor(self, request, v=None):
    #     quakes = Quake.objects.filter(vendor=v)
    #     quakes_json = QuakeSerializer(quakes)
    #     return Response(quakes_json.data, many=True)

    @action(detail=False)
    def highest_mag(self, request):
        vendor = Quake.objects.all().order_by('mag')

        page = self.paginate_queryset(vendor)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(vendor, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def closest_hospitals(self, request):
        """Get hospitals that are at least 3 km from a given location"""
        longitude = request.GET.get('lon', None)
        latitude = request.GET.get('lat', None)

        if longitude and latitude:
            user_location = Point(float(longitude), float(latitude), srid=4326)
            closest_hospitals = Quake.objects.filter(geom__distance_lte=(user_location, D(km=3)))
            serializer = self.get_serializer_class()
            serialized_hospitals = serializer(closest_hospitals, many=True)
            return Response(serialized_hospitals.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
