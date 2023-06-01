from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import *

from compra.api.serializers import CompraSerializer
from compra.models import Compra


class CompraViewSet(GenericViewSet, ListAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated, ]
