import os
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import License
from .licensing import sign_license_payload

class GenerateLicenseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        license_key = request.data.get('license_key')
        valid_until = request.data.get('valid_until')

        if not license_key or not valid_until:
            return Response(
                {'error': 'license_key and valid_until are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        private_key_path = os.path.join('secrets', 'private_key.pem')
        if not os.path.exists(private_key_path):
            return Response(
                {'error': 'Server private key missing. Run key generator first.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        with open(private_key_path, 'rb') as f:
            private_key_pem = f.read()

        payload = json.dumps({
            'license_key': license_key,
            'user_id': request.user.id,
            'valid_until': str(valid_until)
        }).encode('utf-8')

        signature = sign_license_payload(payload, private_key_pem)

        license_obj = License.objects.create(
            user=request.user,
            license_key=license_key,
            public_token=signature,
            valid_until=valid_until,
            status='active'
        )

        return Response({
            'id': str(license_obj.id),
            'license_key': license_obj.license_key,
            'token': signature,
            'valid_until': license_obj.valid_until,
            'status': license_obj.status
        }, status=status.HTTP_201_CREATED)
