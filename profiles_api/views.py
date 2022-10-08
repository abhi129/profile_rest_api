from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers

class HelloApiView(APIView):
    """Test view api"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return the list of aPiView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put , patch ,delete)',
            'Is similar to tradition django view',
            'Is mapped'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            meassage = f'hello {name}'
            return Response({'message': meassage})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE'})
# Create your views here.


class HelloViewSet(viewsets.ViewSet):
    """Test api veiwset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put , patch ,delete)',
            'Is similar to tradition django view',
            'Is mapped'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def create(self, request):
        """Create new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            meassage = f'hello {name}'
            return Response({'message': meassage})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """handle get object"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating the profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


