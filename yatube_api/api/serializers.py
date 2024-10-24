from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор модели подписок."""

    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны.'
            )
        ]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        return data


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели постов."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id', 'text', 'pub_date', 'author',
            'image', 'group', 'comments'
        )
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели групп."""

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'posts')
        model = Group
