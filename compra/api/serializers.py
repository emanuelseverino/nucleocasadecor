from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from compra.models import Compra

Usuario = get_user_model()


class EmpresaSerializer(ModelSerializer):
    class Meta:
        ref_name = "Empresa"
        model = Usuario
        fields = ['foto', 'first_name', 'last_name', 'email', 'tipo']


class EspecificadorSerializer(ModelSerializer):
    class Meta:
        ref_name = "Especificado"
        model = Usuario
        fields = ['foto', 'first_name', 'last_name', 'email', 'tipo']


class CompraSerializer(ModelSerializer):

    class Meta:
        model = Compra
        fields = "__all__"
