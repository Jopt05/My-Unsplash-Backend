from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from images import serializers
from .models import Image
# Create your views here.


class ImagesAuth(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ImageSerializer

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


class DeleteImagesAuth(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.DeleteImageSerializer

    def delete(self, request, pk):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user

            if user.check_password(serializer.data["password"]):
                Image.objects.filter(id=pk).delete()
                return Response(
                    {
                        "msg": "Image deleted!",
                    },
                    status=status.HTTP_202_ACCEPTED
                )

            else:
                return Response(
                    {
                        "msg": "Password is not correct!",
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class Images(APIView):

    serializer_class = serializers.ImageSerializer

    def get(self, request):
        images = Image.objects.all()
        serializer = self.serializer_class(images, many=True)
        return Response(
            data=serializer.data
        )


class ImagesByUser(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ImageSerializer

    def get(self, request, pk):
        images = Image.objects.filter(author=pk)
        serializer = self.serializer_class(images, many=True)
        return Response(
            data=serializer.data
        )
