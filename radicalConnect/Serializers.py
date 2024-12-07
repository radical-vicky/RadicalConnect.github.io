from rest_framework import serializers

from radicalConnect.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','email','phoneNumber','gender','occupation']