from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response({
                'message': 'The snippet has been selected successfully.',
                'data': serializer.data,
                'error': False,
                'errorDetails': None
            })

    elif request.method == 'PUT':
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
                'message': 'The snippet couldn\'t be successfully. There are one or more errors in the data sent.',
                'data': request.data,
                'error': True,
                'errorDetails': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = SnippetSerializer(snippet)
        snippet.delete()
        return Response({
                'message': 'The snippet has been deleted successfully.',
                'data': serializer.data,
                'error': False,
                'errorDetails': None
            }, status=status.HTTP_204_NO_CONTENT)
