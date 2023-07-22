from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPIView


router = DefaultRouter()
router.register('user', UserAPIView, 'api_user')

urlpatterns = router.urls