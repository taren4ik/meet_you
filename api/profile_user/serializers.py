from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Сериализатор модели профайла. """

    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
        )

    class Meta:
        model = Profile
        fields = ('id', 'author', 'phone', 'year', 'image', 'description',
                  'category',
                  )
