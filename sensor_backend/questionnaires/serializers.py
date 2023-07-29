from rest_framework import serializers

from .models import BarthelIndex
from account.serializers import UserSerializer
from patient.serializers import PatientSerializer


def get_total_score(obj):
    return obj.total_score()


class BarthelIndexSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = BarthelIndex
        fields = [
            'patient',
            'created_by',
            'created_at',
            'barthel_food',
            'barthel_wash',
            'barthel_shower',
            'barthel_dress',
            'barthel_stool',
            'barthel_urin',
            'barthel_wc',
            'barthel_transf',
            'barthel_walk',
            'barthel_staris'
        ]
        read_only_fields = ['total_score']

    total_score = serializers.SerializerMethodField()
