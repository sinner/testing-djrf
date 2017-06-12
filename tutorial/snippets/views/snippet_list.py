from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response({
            'message': 'There is no data found.'if(len(serializer.data) == 0)else'There is data found.',
            'data': serializer.data,
            'error': False,
            'errorDetails': None
        })

    elif request.method == 'POST':
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
