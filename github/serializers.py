from rest_framework import serializers
from . import models as github


# ======================
# Tag
# ======================
class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = github.Tag
        fields = ('id_tag','name')


class CreateTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = github.Tag
        fields = ('id_tag','name')


# ======================
# Repositories
# ======================
class RepositorySerializer(serializers.ModelSerializer):
    
    tags = TagSerializer(many=True)

    class Meta:
        model = github.Repository
        fields = ('id_repository','name', 'descriptition', 'tags', 'user')


class CreateRepositorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = github.Repository
        fields = ('id_repository','name', 'descriptition', 'tags', 'user')

