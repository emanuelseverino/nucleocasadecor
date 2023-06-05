from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from compra.models import Compra


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['foto', 'first_name', 'last_name', 'email', 'tipo']


class EspecificadorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['foto', 'first_name', 'last_name', 'email', 'tipo']


class CompraSerializer(ModelSerializer):
    empresa = EmpresaSerializer()
    especificador = EspecificadorSerializer()

    class Meta:
        model = Compra
        fields = "__all__"
