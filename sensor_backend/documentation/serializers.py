from rest_framework import serializers
from .models import *
from account.serializers import UserSerializer
from patient.serializers import PatientSerializer


class InitialExaminationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = InitialExamination
        fields = "__all__"


class InstructionWearableSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = InstructionWearable
        fields = "__all__"


class InitialInterviewTelephoneSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = InitialInterviewTelephone
        fields = "__all__"


class DataReviewProcessingSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = DataReviewProcessing
        fields = "__all__"


class TelephoneConsultationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    consultation_by = UserSerializer(many=True, read_only=True)

    class Meta:
        model = TelephoneConsultation
        fields = "__all__"


class FeedbackCareTeamTelephoneConsultationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = FeedbackCareTeamTelephoneConsultation
        fields = "__all__"


class CaseReviewNurseCouncilSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = CaseReviewNurseCouncil
        fields = "__all__"


class CaseReviewCouncilSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = CaseReviewCouncil
        fields = "__all__"


class CaseReviewSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = CaseReview
        fields = "__all__"


class ConsultationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Consultation
        fields = "__all__"


class VisitSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Visit
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"
