from django.db import models

class UserStudyRating(models.Model):
    name = models.CharField(max_length=16, primary_key=True)

    rating1_1 = models.IntegerField(default=0)
    rating1_2 = models.IntegerField(default=0)
    rating2_1 = models.IntegerField(default=0)
    rating2_2 = models.IntegerField(default=0)
    rating3_1 = models.IntegerField(default=0)
    rating3_2 = models.IntegerField(default=0)
    rating4_1 = models.IntegerField(default=0)
    rating4_2 = models.IntegerField(default=0)
    rating5_1 = models.IntegerField(default=0)
    rating5_2 = models.IntegerField(default=0)

    years_musical_training = models.IntegerField(default=0)
    musical_culture = models.CharField(max_length=16, default='')

    def __str__(self):
        return self.name + "'s rating"


class RatingValue(models.Model):
    value = models.IntegerField(default=0, primary_key=True)

    def __str__(self):
        return str(self.value)