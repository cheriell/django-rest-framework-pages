from django.db import models

class UserStudyRating(models.Model):
    serial_no = models.IntegerField(default=77552330, primary_key=True)

    rating1_1 = models.IntegerField(default=0)
    rating1_2 = models.IntegerField(default=0)
    rating1_3 = models.IntegerField(default=0)
    rating1_4 = models.IntegerField(default=0)
    rating1_5 = models.IntegerField(default=0)

    rating2_1 = models.IntegerField(default=0)
    rating2_2 = models.IntegerField(default=0)
    rating2_3 = models.IntegerField(default=0)
    rating2_4 = models.IntegerField(default=0)
    rating2_5 = models.IntegerField(default=0)

    rating3_1 = models.IntegerField(default=0)
    rating3_2 = models.IntegerField(default=0)
    rating3_3 = models.IntegerField(default=0)
    rating3_4 = models.IntegerField(default=0)
    rating3_5 = models.IntegerField(default=0)

    rating4_1 = models.IntegerField(default=0)
    rating4_2 = models.IntegerField(default=0)
    rating4_3 = models.IntegerField(default=0)
    rating4_4 = models.IntegerField(default=0)
    rating4_5 = models.IntegerField(default=0)

    rating5_1 = models.IntegerField(default=0)
    rating5_2 = models.IntegerField(default=0)
    rating5_3 = models.IntegerField(default=0)
    rating5_4 = models.IntegerField(default=0)
    rating5_5 = models.IntegerField(default=0)

    general_a = models.CharField(max_length=10000, default='')
    general_b = models.CharField(max_length=10000, default='')
    general_c = models.CharField(max_length=10000, default='')

    years_musical_training = models.CharField(max_length=10, default='')
    music_style = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')

    email = models.CharField(max_length=100, default='')
    note = models.CharField(max_length=10000, default='')

    def __str__(self):
        return str(self.serial_no)


class RatingValue(models.Model):
    value = models.IntegerField(default=0, primary_key=True)

    def __str__(self):
        return str(self.value)