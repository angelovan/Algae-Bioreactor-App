from django.db import models
from django.utils import timezone

# Create your models here.

class AlgaeSpecies(models.Model):
  ALGAE_CHOICES = [
      ('Chlorella vulgaris', 'Chlorella vulgaris'),
      ('Arthrospira platensis (Spirulina)','Arthrospira platensis (Spirulina)'),
      ('Scenedesmus obliquus', 'Scenedesmus obliquus'),
  ]

  name = models.CharField(
      max_length=100,
      choices=ALGAE_CHOICES,
      unique=True,
      verbose_name='Strain Name',
  )
  feed_interval_days = models.IntegerField(
      default=7, verbose_name='Nutrient Feed Interval (Days)'
  )
  optimal_temp = models.FloatField(
      default=25.0, verbose_name='Optimal Temperature (°C)'
  )
  target_ph = models.FloatField(default=7.0, verbose_name='Target pH Level')
  description = models.TextField(
      blank=True,
      null=True,
      verbose_name='Algae Strain Description',
  )

  def __str__(self):
      return self.name


class Equipment(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name='Equipment Name'
    )

    def __str__(self):
        return self.name


class BioreactorUnit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Unit Identifier')
    location = models.CharField(max_length=100, verbose_name='Cabinet Location')
    algae_species = models.ForeignKey(
        AlgaeSpecies, on_delete=models.CASCADE, verbose_name='Algae Species'
    )
    equipment = models.ManyToManyField(
        Equipment, related_name='bioreactors', verbose_name='Installed Equipment'
    )
    setup_date = models.DateField(
        default=timezone.localdate, verbose_name='Setup Date'
    )
    progress_photo = models.FileField(
        upload_to='bioreactor_files/',
        blank=True,
        null=True,
        verbose_name='Progress Photo',
    )
    observations = models.TextField(
        blank=True, null=True, verbose_name='Student Observation Notes'
    )

    def __str__(self):
        return f'{self.name} Culturing {self.algae_species.name}'