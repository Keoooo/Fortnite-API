from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('outfits', views.OutfitView)
router.register('season', views.seasonView)
router.register('outfits/<int:id>', views.SingleSkin)


urlpatterns = [
path('', include(router.urls))
]
