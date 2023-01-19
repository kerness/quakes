from django.contrib.gis.db import models


class Quake(models.Model):
    mag = models.FloatField(("Magnitude"))
    date = models.DateField(("Date"))
    geom = models.PointField(srid=4326)
    source_system_id = models.CharField(
        ("ID from source system"), max_length=64, unique=True
    )
    vendor = models.CharField(
        max_length=32,
        choices=[("USGS", "USGS"), ("GRSS", "GRSS"), ("Unknown", "Unknown")],
        default="Unknown",
    )

    def __str__(self) -> str:
        return str(self.mag) + str(self.date)

    # a to nie wystarczy tylko żeby source_system_id było unique? xdd
    def save(self, *args, **kwargs):
        if self.vendor == "GRSS":

            super().save(*args, **kwargs)
        elif self.vendor == "USGS":
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
