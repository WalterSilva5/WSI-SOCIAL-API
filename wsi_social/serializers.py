from rest_framework import serializers
from wsi_social.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)
        write_only_fields = ('password',)