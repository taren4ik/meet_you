from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status

from .models import  Profile
from .serializers import ProfileSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


# class CategoryViewSet(viewsets.ModelViewSet):
#     permission_classes = []
#     queryset = Category.objects.all()
#     serializer_class = ProfileSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Добавление и удаление комментария."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        profile_id = self.kwargs.get('post_id')
        profile = get_object_or_404(Profile, id=profile_id)
        return profile.comments.all()

    def perform_create(self, serializer):
        profile_id = self.kwargs.get('post_id')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(author=self.request.user, profile=profile)


class ProfileAPIView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    """Операции возвращения изменения и  удаления объектов по одному."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)

# class ProfileViewSet(viewsets.ModelViewSet):
#     permission_classes = []
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
