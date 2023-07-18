from rest_framework import serializers
from administracion.models import Reportes


class ReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reportes
        fields = ['calle', 'numero', 'colonia', 'estado', 'ciudad', 'codigo_postal', 'tipo_reporte', 'estatus', 'descripcion']