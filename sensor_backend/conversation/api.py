from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer


@api_view(['GET'])
def get_conversation(request, patient_id):
    try:
        conversation = Conversation.objects.get(patient__id=patient_id)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_message(request, conversation_id):
    user = request.user
    conversation = Conversation.objects.get(id=conversation_id)

    # Check if the user is part of the conversation
    if user not in conversation.users.all():
        return Response({"message": "You are not part of this conversation"}, status=400)

    data = request.data.copy()
    data["conversation"] = str(conversation_id)

    serializer = ConversationMessageSerializer(data=data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=201)
    print("Serializer errors:", serializer.errors)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_messages(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    if request.user not in conversation.users.all():
        return Response({"message": "You are not part of this conversation"}, status=400)

    messages = conversation.message.all()
    serializer = ConversationMessageSerializer(messages, many=True)

    return Response(serializer.data)
