import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Sale, Repair, Customer

class BatchSyncView(APIView):
    def post(self, request):
        records = request.data.get('records', [])
        synced_ids = []

        with transaction.atomic():
            for record in records:
                entity_type = record.get('entity_type')
                payload = json.loads(record.get('payload', '{}'))
                record_id = record.get('id')

                if entity_type == 'sale':
                    Sale.objects.update_or_create(
                        id=record_id,
                        defaults={
                            'total_amount': payload.get('total_amount'),
                            'profit': payload.get('profit'),
                            'synced': True
                        }
                    )
                    synced_ids.append(record_id)

                elif entity_type == 'repair':
                    customer, _ = Customer.objects.get_or_create(
                        id=payload.get('customer_id'),
                        defaults={'name': payload.get('customer_name', 'Walk-in')}
                    )
                    Repair.objects.update_or_create(
                        id=record_id,
                        defaults={
                            'customer': customer,
                            'device_info': payload.get('device_info'),
                            'cost': payload.get('cost'),
                            'payment': payload.get('payment'),
                            'status': payload.get('status', 'received'),
                            'synced': True
                        }
                    )
                    synced_ids.append(record_id)

        return Response({'status': 'success', 'synced_ids': synced_ids}, status=status.HTTP_200_OK)
