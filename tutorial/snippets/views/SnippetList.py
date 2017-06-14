from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response({
                'message': 'The snippet has been selected successfully.',
                'data': serializer.data,
                'error': False,
                'errorDetails': None
            })

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'The snippet has been saved successfully.',
                'data': serializer.data,
                'error': False,
                'errorDetails': None
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are one or more errors in the data sent.',
            'data': request.data,
            'error': True,
            'errorDetails': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
