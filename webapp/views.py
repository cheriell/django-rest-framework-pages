from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import UserStudyRating, RatingValue

def index(request):
    context = {}
    return render(request, 'index.html', context)

def consent_form(request):
    context = {}
    return render(request, 'consent_form.html', context)

def user_study(request):
    rating_values = RatingValue.objects.all()
    context = {
        'rating_values': rating_values,
        'segments': [
            {'no': '1', 'name': 'mond_2_segment1', 'left': 'true' },
            {'no': '2', 'name': 'chp_op18_segment1', 'left': 'false'},
            {'no': '3', 'name': 'viennese1-4_segment1', 'left': 'true' },
            {'no': '4', 'name': 'tmte04-63j_segment1', 'left': 'false'},
            {'no': '5', 'name': 'clementi_opus36_5_3_segment1', 'left': 'true' },
        ],
        'music_styles': [
            {'value': 'African'},
            {'value': 'Arabic Music'},
            {'value': 'Asian'},
            {'value': 'Blues'},
            {'value': 'Country'},
            {'value': 'Electronic Music'},
            {'value': 'Folk'},
            {'value': 'Hip Hop'},
            {'value': 'Jazz'},
            {'value': 'Latin'},
            {'value': 'Pop'},
            {'value': 'Rock'},
            {'value': 'Western Classical Music'},
            {'value': 'Other'},
        ],
    }
    return render(request, 'user_study.html', context)

def thanks(request):
    rating1_1 = request.POST['rating1_1']
    rating1_2 = request.POST['rating1_2']

    rating2_1 = request.POST['rating2_1']
    rating2_2 = request.POST['rating2_2']

    rating3_1 = request.POST['rating3_1']
    rating3_2 = request.POST['rating3_2']

    rating4_1 = request.POST['rating4_1']
    rating4_2 = request.POST['rating4_2']

    rating5_1 = request.POST['rating5_1']
    rating5_2 = request.POST['rating5_2']

    general_a = request.POST['general_a']
    general_b = request.POST['general_b']
    general_c = request.POST['general_c']

    years_musical_training = request.POST['years_musical_training']
    music_style = request.POST['music_style']
    name = request.POST['name']
    email = request.POST['email']

    user_study_rating = UserStudyRating(rating1_1=rating1_1, rating1_2=rating1_2, rating2_1=rating2_1, rating2_2=rating2_2, rating3_1=rating3_1, rating3_2=rating3_2, rating4_1=rating4_1, rating4_2=rating4_2, rating5_1=rating5_1, rating5_2=rating5_2, general_a=general_a, general_b=general_b, general_c=general_c, years_musical_training=years_musical_training, music_style=music_style, name=name, email=email)

    user_study_ratings = UserStudyRating.objects.all()

    last_rating = UserStudyRating()
    for r in user_study_ratings:
        last_rating = r

    if (serialise(user_study_rating) != serialise(last_rating)) :
        user_study_rating.serial_no = last_rating.serial_no + 1
        user_study_rating.save()
    else:
        user_study_rating.serial_no = last_rating.serial_no
    
    context = {
        'name': name,
        'serial_no': user_study_rating.serial_no,
    }
    return render(request, 'thanks.html', context)

def serialise(r):
    # serialise an UserStudyRating's information except for its seiral_no
    result = ''
    result += str(r.rating1_1) + str(r.rating1_2)
    result += str(r.rating2_1) + str(r.rating2_2)
    result += str(r.rating3_1) + str(r.rating3_2)
    result += str(r.rating4_1) + str(r.rating4_2)
    result += str(r.rating5_1) + str(r.rating5_2)

    result += r.general_a + r.general_b + r.general_c

    result += r.years_musical_training
    result += r.music_style
    result += r.name
    result += r.email

    return result

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer