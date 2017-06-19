from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView
from snippets.serializers.UserSerializer import UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
