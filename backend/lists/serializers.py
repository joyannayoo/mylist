from rest_framework import serializers
from lists.models from List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'
