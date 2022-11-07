from email.policy import default
from random import choices
from django.contrib.gis.db import models

# class DataVendor(models.Model):
#     name = models.TextField(("Data Vendor name"))

#     def __str__(self) -> str:
#         return self.name


class Quake(models.Model):
    mag = models.FloatField(("Magnitude"))
    date = models.DateField(("Date"))
    geom = models.PointField(srid=4326)
    # vendor = models.ForeignKey(DataVendor, on_delete=models.CASCADE, default=1)
    vendor = models.CharField(
        max_length=32,
        choices=[("USGS", "USGS"), ("GRSS", "GRSS"), ("Unknown", "Unknown")],
        default="Unknown",
    )

    def __str__(self) -> str:
        return str(self.mag) + str(self.date)
        