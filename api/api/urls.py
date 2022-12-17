from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('profile_user.urls')),
    path('', include('frontend.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
]
