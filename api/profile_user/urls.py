from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import CommentViewSet, ProfileAPIView, ProfileAPIDetail

router = SimpleRouter()
router.register(
    r'^profiles/(?P<profile_id>\d+)/comments', CommentViewSet,
    basename='profile')

urlpatterns = [
    path('profiles/<int:pk>/', ProfileAPIDetail.as_view()),
    path('profiles/', ProfileAPIView.as_view()),
    path('', include(router.urls)),
]
