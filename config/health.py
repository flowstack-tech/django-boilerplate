from api.common.responses import OkResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckDetail(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        return Response(OkResponse('Health Check Successful').get_response(), status=status.HTTP_200_OK)
