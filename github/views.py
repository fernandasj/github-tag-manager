from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models as github
from . import serializers

class RepositoryViewSet(viewsets.ModelViewSet):

    queryset = github.Repository.objects.all()
    serializer_class = serializers.CreateRepositorySerializer

    # def create(self, resquest):
    #     for tag in request.data['tags']:
    #         newTag = github.Tag.objects.create(name=tag)
        

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.RepositorySerializer
        return super().get_serializer_class()