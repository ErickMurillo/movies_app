from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.db.models import Avg

# Create your views here.
class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.annotate(rating=Avg('review__rating')).order_by('-released_on','-rating')

