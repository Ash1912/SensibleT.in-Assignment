from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    # Format timestamp to the desired format
    timestamp = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%SZ')
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'status', 'timestamp', 'user']
def update(self, instance, validated_data):
        # Update only provided fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance