from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import UserStudyRating

def index(request):
    ratings = UserStudyRating.objects.all()
    context = {
        'ratings': ratings,
    }
    return render(request, 'index.html', context)


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