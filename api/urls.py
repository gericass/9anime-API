from rest_framework import routers
from .views import animedbViewSet

router = routers.DefaultRouter()
router.register(r'',animedbViewSet)