from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

from .forms import SignupForm


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
    else:
        message = 'error'

    return JsonResponse({'message': message})


@api_view(['GET'])
def doctor_list(request):
    doctors = User.objects.filter(role='DR')
    serializer = UserSerializer(doctors, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def nurse_list(request):
    nurses = User.objects.filter(role='NR')
    serializer = UserSerializer(nurses, many=True, context={'request': request})
    return Response(serializer.data)
