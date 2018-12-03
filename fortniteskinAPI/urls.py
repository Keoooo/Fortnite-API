"""fortniteskinAPI URL Configuration

Imported setting and static to make image show on json request from uploaded image
Future: posible have the images from a web server and get via url

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from api import views
from django.conf.urls.static import static
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.apihome, name='apihome'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('about/', include('about.urls'), name='about'),
    path('docs/', include('docs.urls'), name='docs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
