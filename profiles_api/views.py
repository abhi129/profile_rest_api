from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test view api"""

    def get(self, request, format=None):
        """Return the list of aPiView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put , patch ,delete)',
            'Is similar to tradition django view',
            'Is mapped'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})



# Create your views here.
