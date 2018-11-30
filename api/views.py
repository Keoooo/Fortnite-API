from django.shortcuts import render
from rest_framework import viewsets
from .models import fortniteskins
from .serializer import SkinSerializer


class OutfitView(viewsets.ModelViewSet):
	queryset = fortniteskins.objects.all()
	serializer_class = SkinSerializer

def apihome(request):
	skins = fortniteskins.objects
	return render(request, 'apihome/index.html', {'forntiteskins':skins})
