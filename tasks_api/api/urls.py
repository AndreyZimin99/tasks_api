from django.urls import include, path
from rest_framework import routers

from api.views import (
    TaskViewSet
)

router_v1 = routers.DefaultRouter()
router_v1.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router_v1.urls)),
]
