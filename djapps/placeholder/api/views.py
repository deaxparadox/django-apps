from rest_framework import generics

from .serializers import UserInfoSerializer
from ..models import UserInfo

class ListView(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
