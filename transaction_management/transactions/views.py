from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # Action to get transactions by user_id
    @action(detail=False, methods=['get'])
    def by_user(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id query parameter is required."}, status=400)

        # Filter transactions by user_id
        transactions = Transaction.objects.filter(user_id=user_id)

        # Optionally filter by status (PENDING, COMPLETED)
        status = request.query_params.get('status', None)
        if status:
            transactions = transactions.filter(status=status)

        # Serialize the transactions
        serializer = self.get_serializer(transactions, many=True)

        # Return the response with a "transactions" key
        return Response({"transactions": serializer.data})
    
     # To allow partial updates for PUT/PATCH
    def update(self, request, *args, **kwargs):
        partial = kwargs.get('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


