from rest_framework import routers

from . import views as api

app_name = 'github-api'

router = routers.DefaultRouter()
router.register(r'repositories', api.RepositoryViewSet, basename='api-github')

urlpatterns = router.urls