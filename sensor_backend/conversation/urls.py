from django.urls import path
from . import api

urlpatterns = [
    path('<uuid:patient_id>/', api.get_conversation, name='conversation'),
    path('<uuid:conversation_id>/message/', api.create_message, name='create_message'),
    path('<uuid:conversation_id>/messages/', api.get_messages, name='get_message'),

]
