from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


@api_view(['POST'])
def create_initial_examination(request):
    serializer = InitialExaminationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_instruction_wearable(request):
    serializer = InstructionWearableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_initial_interview_telephone(request):
    serializer = InitialInterviewTelephoneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_data_review_processing(request):
    serializer = DataReviewProcessingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_telephone_consultation(request):
    serializer = TelephoneConsultationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_feedback_care_team_telephone_consultation(request):
    serializer = FeedbackCareTeamTelephoneConsultationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_case_review_nurse_council(request):
    serializer = CaseReviewNurseCouncilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_case_review_council(request):
    serializer = CaseReviewCouncilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_case_review(request):
    serializer = CaseReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_consultation(request):
    serializer = ConsultationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_visit(request):
    serializer = VisitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_equipment(request):
    serializer = EquipmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_initial_examinations(request):
    examinations = InitialExamination.objects.all()
    serializer = InitialExaminationSerializer(examinations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_instruction_wearables(request):
    wearables = InstructionWearable.objects.all()
    serializer = InstructionWearableSerializer(wearables, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_initial_interview_telephones(request):
    interviews = InitialInterviewTelephone.objects.all()
    serializer = InitialInterviewTelephoneSerializer(interviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_data_review_processings(request):
    processings = DataReviewProcessing.objects.all()
    serializer = DataReviewProcessingSerializer(processings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_telephone_consultations(request):
    consultations = TelephoneConsultation.objects.all()
    serializer = TelephoneConsultationSerializer(consultations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_feedback_care_team_telephone_consultations(request):
    feedbacks = FeedbackCareTeamTelephoneConsultation.objects.all()
    serializer = FeedbackCareTeamTelephoneConsultationSerializer(feedbacks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_case_review_nurse_councils(request):
    councils = CaseReviewNurseCouncil.objects.all()
    serializer = CaseReviewNurseCouncilSerializer(councils, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_case_review_councils(request):
    reviews = CaseReviewCouncil.objects.all()
    serializer = CaseReviewCouncilSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_case_reviews(request):
    reviews = CaseReview.objects.all()
    serializer = CaseReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_consultations(request):
    consultations = Consultation.objects.all()
    serializer = ConsultationSerializer(consultations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_visits(request):
    visits = Visit.objects.all()
    serializer = VisitSerializer(visits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_equipments(request):
    equipments = Equipment.objects.all()
    serializer = EquipmentSerializer(equipments, many=True)
    return Response(serializer.data)
