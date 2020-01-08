# example/views.py
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import ExampleBucketlistSerializer
from .models import ExampleBucketlist


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ExampleBucketlist.objects.all()
    serializer_class = ExampleBucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = ExampleBucketlist.objects.all()
    serializer_class = ExampleBucketlistSerializer
