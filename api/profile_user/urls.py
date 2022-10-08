from django.urls import path
from .views import ProfileAPIView, ProfileAPIDetail

urlpatterns = [
    path('profiles/<int:pk>/', ProfileAPIDetail.as_view()),
    path('profiles/', ProfileAPIView.as_view())
]
