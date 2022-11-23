import datetime as dt

from rest_framework import serializers

from .models import  Comment, User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Сериализатор модели профайла. """

    age = serializers.SerializerMethodField()

    # comments = serializers.SlugRelatedField(
    #     slug_field='author',
    #     queryset=User.objects.all(),
    # )
    # category = serializers.SlugRelatedField(
    #     slug_field='category',
    #     queryset=Category.objects.all(),
    # )

    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Profile
        fields = ('id', 'author', 'phone', 'year', 'age', 'sex', 'image',
                  'description', 'category', 'city', 'comments'
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


# class CategorySerializer(serializers.ModelSerializer):
#     """ Сериализатор модели категории. """
#
#     class Meta:
#         model = Category
#         fields = '__all__'
