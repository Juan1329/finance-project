from rest_framework import serializers
from .models import Cliente, Cobranca

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class CobrancaSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')

    class Meta:
        model = Cobranca
        fields = '__all__'
