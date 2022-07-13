from rest_framework import viewsets
from . import models
from . import serializers


class ProfileViewset(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class MerchandiseViewset(viewsets.ModelViewSet):
    queryset = models.Merchandise.objects.all()
    serializer_class = serializers.MerchandiseSerializer

class FeedsViewset(viewsets.ModelViewSet):
    queryset = models.Feeds.objects.all()
    serializer_class = serializers.FeedsSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer



