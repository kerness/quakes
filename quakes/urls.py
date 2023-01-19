from django.urls import path
from quakes import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("quakes/", views.QuakeList.as_view()),
    path("quakes/<int:pk>/", views.QuakeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
