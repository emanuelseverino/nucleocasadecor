from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

Usuario = get_user_model()


class EmpresasSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['foto', 'nome', 'cidade', ]
