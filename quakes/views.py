from rest_framework import viewsets
from .models import Quake
from .serializers import QuakeSerializer

class QuakeViewSet(viewsets.ModelViewSet):
    queryset = Quake.objects.all()
    serializer_class = QuakeSerializer
