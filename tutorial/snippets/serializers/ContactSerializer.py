from rest_framework import serializers
from snippets.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'name', 'profile_picture_url')
