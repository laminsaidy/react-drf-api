from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import YourCustomSerializer
from datetime import datetime

class YourDataView(APIView):
    def get(self, request):
        data = {
            "id": 1,
            "name": "Sample Item",
            "created": datetime.now(),
            "updated": datetime.now()
        }
        
        serializer = YourCustomSerializer(data)
        return Response(serializer.data)



@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my drf API!"
    })