from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from snippets.serializers.UserSerializer import UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
