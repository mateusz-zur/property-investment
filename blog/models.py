from django.db import models
from django.utils import timezone


class Investment(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    time_range = models.IntegerField(editable = False, default=2)
    title = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.IntegerField()
    price_per_unit = models.IntegerField()
    minimal_investment = models.IntegerField()
    percent = models.CharField(max_length=3)

    def add(self):
        self.time_range = self.end_date - self.start_date
        self.save()

    def __str__(self):
        return self.title + ' ' + self.description
