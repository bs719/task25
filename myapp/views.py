from django.http import JsonResponse
from .serializers import MySerializer

def my_view(request):
    data = {'message': 'воображение'}
    serializer = MySerializer(data=data)
    if serializer.is_valid():
        return JsonResponse(serializer.data)
    else:
        return JsonResponse(serializer.errors, status=400)
