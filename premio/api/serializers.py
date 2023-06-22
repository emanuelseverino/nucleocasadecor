from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer

from premio.models import Premio


class PremioSerializer(ModelSerializer):

    imagem_1 = Base64ImageField(requerid=True)
    imagem_2 = Base64ImageField(requerid=False)
    imagem_3 = Base64ImageField(requerid=False)
    imagem_4 = Base64ImageField(requerid=False)
    imagem_5 = Base64ImageField(requerid=False)
    imagem_6 = Base64ImageField(requerid=False)

    class Meta:
        model = Premio
        fields = "__all__"
