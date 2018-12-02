from django.shortcuts import render
from rest_framework import viewsets
from .models import fortniteskins, season
from ratelimit.decorators import ratelimit
from rest_framework.throttling import ScopedRateThrottle
from .pagination import GetLimitOffsetPagination
from .serializer import SkinSerializer, SeasonSerializer


class OutfitView(viewsets.ModelViewSet):
	""" Returns a view off all the skins"""
	pagination_class = GetLimitOffsetPagination
	queryset = fortniteskins.objects.all()
	serializer_class = SkinSerializer
	throttle_scope = 'skinrequest'
	throttle_classes = (ScopedRateThrottle,)


class seasonView(viewsets.ModelViewSet):
	""" Returns a view off all the seasons and themes and date"""
	queryset = season.objects.all()
	serializer_class = SeasonSerializer
	throttle_scope = 'skinrequest'
	throttle_classes = (ScopedRateThrottle,)

class SingleSkin(viewsets.ModelViewSet):
	""" SIngle Skin"""
	serializer_class = fortniteskins.objects.all()
	queryset = fortniteskins.objects.all()
	lookup_field = 'id'


def apihome(request):
	skins = fortniteskins.objects
	return render(request, 'apihome/index.html', {'forntiteskins':skins})

