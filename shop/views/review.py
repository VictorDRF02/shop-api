from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers import ReviewSerializer
from ..models import Review

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
