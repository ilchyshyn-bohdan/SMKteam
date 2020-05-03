from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('grid/<int:zoom>/<int:grid_size>/', csrf_exempt(views.GridCluster.as_view()), name='grid_cluster'),
    path('kmeans/<int:zoom>/<int:grid_size>/', csrf_exempt(views.KmeansCluster.as_view()), name='kmeans_cluster'),
    path('getClusterContent/<int:zoom>/<int:grid_size>/', csrf_exempt(views.GetClusterContent.as_view()),
         name='get_cluster_content'),
    path('getAreaContent/<int:zoom>/<int:grid_size>/', csrf_exempt(views.GetAreaContent.as_view()),
         name='get_area_content'),
]
