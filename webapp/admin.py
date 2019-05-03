from django.contrib import admin
from .models import UserStudyRating, RatingValue

admin.site.register(UserStudyRating)
admin.site.register(RatingValue)
