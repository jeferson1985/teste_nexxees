from .models import Livro
from rest_framework import serializers

class LivrosSerializer(serializers.ModelSerializer):
    disponivel = serializers.ReadOnlyField()
    class Meta:
        model = Livro
        exclude = ['em_estoque']