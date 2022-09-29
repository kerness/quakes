from django.contrib.gis.db import models

class Quake(models.Model):
    mag = models.FloatField(('Magnitude'))
    date = models.DateTimeField(('Time and date'))
    geom = models.PointField(srid=4326)

    def __str__(self) -> str:
        return str(self.mag) + str(self.date)
    