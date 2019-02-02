from django.db import models

class UserStudyRating(models.Model):
    name = models.CharField(max_length=16, primary_key=True)
    rating_1 = models.IntegerField(default=0)
    rating_2 = models.IntegerField(default=0)

    def __str__(self):
        return self.name + "'s rating"
