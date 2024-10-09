from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
  '', TaskViewSet, basename='task'
)

# urlpatterns = [] + router.urls

urlpatterns = [
  path('', include(router.urls)),
]