from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['POST'])
def filter(request):
    data = request.data
    query = data('query')
    print('query', query)

    return JsonResponse({'test': 'test'})
