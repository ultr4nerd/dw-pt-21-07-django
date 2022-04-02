"""Songs app URL configuration"""

from rest_framework import routers

from . import views

app_name = "songs"

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewset, basename='song')
router.register(r'albums', views.AlbumViewset, basename='album')
router.register(r'artists', views.ArtistViewset, basename='artist')

urlpatterns = router.urls
