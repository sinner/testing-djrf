from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response({
                'message': 'The snippet has been found successfully.',
                'data': serializer.data,
                'error': False,
                'errorDetails': None
            })

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'The snippet has been updated successfully.',
                'data': serializer.data,
                'error': False,
                'errorDetails': None
            })
        return Response({
            'message': 'There are one or more errors in the data sent.',
            'data': request.data,
            'error': True,
            'errorDetails': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        snippet.delete()
        return Response({
                'message': 'The snippet has been deleted successfully.',
                'data': serializer.data,
                'error': False,
                'errorDetails': None
            }, status=status.HTTP_204_NO_CONTENT)
