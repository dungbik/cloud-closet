
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import User


@csrf_exempt
def test(request):
    print(request.META)
    if request.user.is_authenticated:
        return JsonResponse({'success': True, 'msg': '인증 성공'}, status=200)
    else:
        return JsonResponse({'success': False, 'msg': '인증 실패.'}, status=200)
