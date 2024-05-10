from rest_framework import serializers
from ..models import Review, User

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ReviewSerializer(serializers.ModelSerializer):
    User = UserReviewSerializer(read_only=True, source='user')
    class Meta:
        model = Review
        fields = ['id', 'user', 'User', 'product', 'rating', 'comment']