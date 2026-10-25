from django.db import models
from django.utils import timezone
from bioreactors.models import BioreactorUnit

# Create your models here.

class ExperimentLog(models.Model):
    date_recorded = models.DateTimeField(default=timezone.now, verbose_name="Measurement Date")
    measured_ph = models.FloatField(verbose_name="Measured pH Level")
    measured_temp = models.FloatField(verbose_name="Temperature (°C)")
    notes = models.TextField(blank=True, null=True, verbose_name="Lab Notes")

    bioreactor = models.ForeignKey(BioreactorUnit, on_delete=models.CASCADE, related_name="logs",
                                   verbose_name="Bioreactor Unit")

    def __str__(self):
        return f"Log for {self.bioreactor.name} on {self.date_recorded}"


class NutrientFeed(models.Model):
    bioreactor = models.ForeignKey(BioreactorUnit, on_delete=models.CASCADE, related_name="feeds",
                                   verbose_name="Bioreactor Unit")
    due_date = models.DateField(verbose_name="Feed Due Date")
    is_completed = models.BooleanField(default=False, verbose_name="Feed Completed?")
    completed_date = models.DateField(blank=True, null=True, verbose_name="Date Feed Completed")
    notes = models.TextField(blank=True, null=True, verbose_name="Feeding Notes")

    def __str__(self):
        status = f"Completed on {self.completed_date}" if self.is_completed else "Pending"
        return f"Feed for {self.bioreactor.name} due {self.due_date} [{status}]"