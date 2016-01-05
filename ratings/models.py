from django.db import models

class Rating(models.Model):
    user_id = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=5)
    last_modified = models.DateField(auto_now_add=True)
    total = models.IntegerField(default=3)
    culture = models.IntegerField(default=3)
    infrastructure = models.IntegerField(default=3)
    green = models.IntegerField(default=3)
    safety = models.IntegerField(default=3)

    class Meta:
        ordering = ('last_modified',)
        unique_together = ('user_id', 'zipcode')
