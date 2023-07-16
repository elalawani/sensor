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
    queryset = models.InstructionWearable.objects.all()
    serializer_class = InstructionWearableSerializer


class InstructionWearableRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InstructionWearable.objects.all()
    serializer_class = InstructionWearableSerializer


class InitialInterviewTelephoneListCreate(generics.ListCreateAPIView):
    queryset = models.InitialInterviewTelephone.objects.all()
    serializer_class = InitialInterviewTelephoneSerializer


class InitialInterviewTelephoneRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InitialInterviewTelephone.objects.all()
    serializer_class = InitialInterviewTelephoneSerializer


class DataReviewProcessingListCreate(generics.ListCreateAPIView):
    queryset = models.DataReviewProcessing.objects.all()
    serializer_class = DataReviewProcessingSerializer


class DataReviewProcessingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DataReviewProcessing.objects.all()
    serializer_class = DataReviewProcessingSerializer


class TelephoneConsultationListCreate(generics.ListCreateAPIView):
    queryset = models.TelephoneConsultation.objects.all()
    serializer_class = TelephoneConsultationSerializer


class TelephoneConsultationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TelephoneConsultation.objects.all()
    serializer_class = TelephoneConsultationSerializer


class FeedbackCareTeamTelephoneConsultationListCreate(generics.ListCreateAPIView):
    queryset = models.FeedbackCareTeamTelephoneConsultation.objects.all()
    serializer_class = FeedbackCareTeamTelephoneConsultationSerializer


class FeedbackCareTeamTelephoneConsultationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FeedbackCareTeamTelephoneConsultation.objects.all()
    serializer_class = FeedbackCareTeamTelephoneConsultationSerializer


class CaseReviewNurseCouncilListCreate(generics.ListCreateAPIView):
    queryset = models.CaseReviewNurseCouncil.objects.all()
    serializer_class = CaseReviewNurseCouncilSerializer


class CaseReviewNurseCouncilRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CaseReviewNurseCouncil.objects.all()
    serializer_class = CaseReviewNurseCouncilSerializer


class CaseReviewCouncilListCreate(generics.ListCreateAPIView):
    queryset = models.CaseReviewCouncil.objects.all()
    serializer_class = CaseReviewCouncilSerializer


class CaseReviewCouncilRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CaseReviewCouncil.objects.all()
    serializer_class = CaseReviewCouncilSerializer


class CaseReviewListCreate(generics.ListCreateAPIView):
    queryset = models.CaseReview.objects.all()
    serializer_class = CaseReviewSerializer


class CaseReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CaseReview.objects.all()
    serializer_class = CaseReviewSerializer


class ConsultationListCreate(generics.ListCreateAPIView):
    queryset = models.Consultation.objects.all()
    serializer_class = ConsultationSerializer


class ConsultationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Consultation.objects.all()
    serializer_class = ConsultationSerializer


class VisitListCreate(generics.ListCreateAPIView):
    queryset = models.Visit.objects.all()
    serializer_class = VisitSerializer


class VisitRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Visit.objects.all()
    serializer_class = VisitSerializer


class EquipmentListCreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
