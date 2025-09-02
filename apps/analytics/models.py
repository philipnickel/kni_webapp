from django.db import models


class AnalyticsDaily(models.Model):
    site = models.ForeignKey("wagtailcore.Site", on_delete=models.CASCADE)
    date = models.DateField()
    path = models.CharField(max_length=255, blank=True, null=True)
    views = models.IntegerField(default=0)
    uniques = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)

    class Meta:
        unique_together = ("site", "date", "path")

