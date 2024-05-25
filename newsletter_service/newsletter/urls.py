from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriberViewSet, TopicViewSet, ContentViewSet

router = DefaultRouter()
router.register(r'subscribers', SubscriberViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
