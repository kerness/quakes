from rest_framework.routers import DefaultRouter

from .views import QuakeViewSet

router = DefaultRouter()

router.register(prefix='api/v1/quakes', viewset=QuakeViewSet, basename='quake')

urlpatterns = router.urls

