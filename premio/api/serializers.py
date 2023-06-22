from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer

from premio.models import Premio


class PremioSerializer(ModelSerializer):

    class Meta:
        model = Premio
        fields = "__all__"
