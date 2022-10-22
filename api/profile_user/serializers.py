import datetime as dt

from rest_framework import serializers

from .models import Comment, User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Сериализатор модели профайла. """

    age = serializers.SerializerMethodField()

    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Profile
        fields = ('id', 'author', 'phone', 'year', 'age', 'sex', 'image',
                  'description', 'category', 'city',
                  )

    def get_age(self, obj):
        return dt.datetime.now().year - obj.year


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализатор модели профайла. """

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
