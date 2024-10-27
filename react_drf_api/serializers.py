from rest_framework import serializers
from datetime import datetime

class YourCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    created = serializers.DateTimeField(default=datetime.now, read_only=True)
    updated = serializers.DateTimeField(default=datetime.now, read_only=True)

    # Optionally, customize the create/update times based on your logic
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created'] = data.get('created', datetime.now())
        data['updated'] = datetime.now()
        return data