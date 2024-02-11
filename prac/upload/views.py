from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadSerializer


class UploadApi(APIView):
    def post(self,request):
        data = request.data
        serializer = UploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

