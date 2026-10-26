from datetime import timedelta
from django.db import models
from bioreactors.models import BioreactorUnit


class NutrientFeed(models.Model):
    bioreactor = models.ForeignKey(
        BioreactorUnit,
        on_delete=models.CASCADE,
        related_name='feeds'
    )

    completed_date = models.DateField(verbose_name="Feed Completion Date", blank=True, null=True)
    due_date = models.DateField(verbose_name="Next Feed Due Date", blank=True, null=True)
    is_completed = models.BooleanField(default=False, verbose_name="Feed Completed?")
    notes = models.TextField(blank=True, null=True, verbose_name="Feeding Notes")

    def save(self, *args, **kwargs):
        if self.completed_date:
            self.due_date = self.completed_date + timedelta(days=7)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Feed for {self.bioreactor.name} - Due: {self.due_date}"