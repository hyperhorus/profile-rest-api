from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = ['Uses HTTP methods as function (get, post, patch, put, delete ',
                      'Is similar to traditional Django View',
                      'Gives you the most control over your application logic ',
                      'Is mapped manually to URL'
                      ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})


    def post(self, request):
        """Create Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of the object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})



# Create your views here.
class MyTestView(APIView):
    """This is my own test"""

    def get(self, request, format=None):
        """return something here"""
        my_view = [
            'This is a test of my own',
            'Quiero ver que funciones de otra forma',
            'para ir aprendiendo mas y mas'

                   ]
        return Response({'mensaje':'Mensaje de Weri', 'una vista':my_view})