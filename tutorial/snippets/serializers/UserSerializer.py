from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Contact
from snippets.models import Snippet
from snippets.serializers import ContactSerializer


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    contact = ContactSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'contact', 'snippets')

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        user = User.objects.create(**validated_data)
        Contact.objects.create(user=user, **contact_data)
        return user
