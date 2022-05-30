from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from images import serializers
from .models import Image
# Create your views here.


class Images(APIView):

    serializer_class = serializers.ImageSerializer

    def get(self, request):
        images = Image.objects.all()
        serializer = self.serializer_class(images, many=True)
        return Response(
            data=serializer.data
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class ImagesByUser(APIView):

    serializer_class = serializers.ImageSerializer

    def get(self, request, pk):
        images = Image.objects.filter(author=pk)
        serializer = self.serializer_class(images, many=True)
        return Response(
            data=serializer.data
        )
