from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status

from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly


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
    #permission_classes = (IsOwnerOrReadOnly,)
