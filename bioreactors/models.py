from django.db import models
from django.utils import timezone

# Create your models here.

class AlgaeSpecies(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Algae Strain Name")
    scientific_name = models.CharField(max_length=150, verbose_name="Scientific Name")
    feed_interval_days = models.IntegerField(default=30, verbose_name="Nutrient Feed Interval (Days)")
    optimal_temp = models.FloatField(verbose_name="Optimal Temperature (°C)")
    target_ph = models.FloatField(verbose_name="Target pH Level")
    description = models.TextField(verbose_name="Algae Strain Description")

    def __str__(self):
        return f"{self.name} ({self.scientific_name})"


class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Equipment Name")
    model_number = models.CharField(max_length=50, verbose_name="Model Number")

    def __str__(self):
        return f"{self.name} [{self.model_number}]"


class BioreactorUnit(models.Model):
    name = models.CharField(max_length=100, verbose_name="Unit Identifier")
    location = models.CharField(max_length=100, verbose_name="Cabinet Location")

    species = models.ForeignKey(AlgaeSpecies, on_delete=models.PROTECT, related_name="bioreactors", verbose_name="Selected Algae Type")

    equipment = models.ManyToManyField(Equipment, related_name="bioreactors", verbose_name="Installed Equipment")

    setup_date = models.DateTimeField(default=timezone.now, verbose_name="Setup Date")
    progress_photo = models.FileField(upload_to='bioreactor_files/', blank=True, null=True, verbose_name="Progress Photo")
    observations = models.TextField(blank=True, null=True, verbose_name="Student Observation Notes")

    def __str__(self):
        return f"{self.name} - Culturing {self.species.name}"