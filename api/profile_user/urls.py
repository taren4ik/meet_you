from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import (CommentViewSet, ProfileAPIDetail,
                    ProfileAPIView)


router = SimpleRouter()

# router.register(r'^profiles', ProfileViewSet)
router.register(
    r'^profiles/(?P<profile_id>\d+)/comments', CommentViewSet,
    basename='profile')

# router.register(
#     r'^profiles/(?P<profile_id>\d+)/category', CategoryViewSet)



urlpatterns = [
    path('profiles/', ProfileAPIView.as_view()),
    path('profiles/<int:pk>/', ProfileAPIDetail.as_view()),
    path('', include(router.urls)),
]
