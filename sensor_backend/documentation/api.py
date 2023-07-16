from rest_framework import generics
from .serializers import *
from . import models


class InitialExaminationListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class InitialExaminationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class InstructionWearableListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class InstructionWearableRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class InitialInterviewTelephoneListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class InitialInterviewTelephoneRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class DataReviewProcessingListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class DataReviewProcessingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class TelephoneConsultationListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class TelephoneConsultationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class FeedbackCareTeamTelephoneConsultationListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class FeedbackCareTeamTelephoneConsultationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class CaseReviewNurseCouncilListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class CaseReviewNurseCouncilRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class CaseReviewCouncilListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class CaseReviewCouncilRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class CaseReviewListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class CaseReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class ConsultationListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class ConsultationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class VisitListCreate(generics.ListCreateAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class VisitRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialExamination.objects.all()
    serializer_class = InitialExaminationSerializer


class EquipmentListCreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
