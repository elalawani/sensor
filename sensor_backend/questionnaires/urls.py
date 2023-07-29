from django.urls import path
from .api import create_barthel_index, get_barthel_indexes, barthel_index_detail, barthel_index_choices

urlpatterns = [
    path('<uuid:patient_id>/barthel_indexes/', create_barthel_index, name='create-barthel-index'),
    path('<uuid:patient_id>/barthel_indexes/', get_barthel_indexes, name='get-barthel-indexes'),
    path('barthelindex_choices/', barthel_index_choices, name='barthel_index_choices'),
    path('<uuid:patient_id>/barthel_indexes/<int:barthel_index_id>/', barthel_index_detail, name='barthel-index-detail')
]
