import json


from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from celery.result import AsyncResult

from .models import UserInfo
from .tasks import add, generate_fake_data


# def index(request):
#     qs = UserInfo.objects.all()
#     qs_json = serializers.serialize('json', qs)
#     return HttpResponse(qs_json, content_type='application/json')

def index(request):
    qs = UserInfo.objects.all()
    return render(request, "placeholder/index.html", {
        "userinfo": qs,
    })

def get_user(request, id):
    qs = get_object_or_404(UserInfo, id=id)
    return JsonResponse(
        qs.to_dict(), status=200
    )

def addview(request):
    limit = request.GET.get("limit")
    result = generate_fake_data.delay(int(limit))
    return JsonResponse({
        "id": result.id
    }, status=200)

def statusview(request, id):
    result = AsyncResult(id)
    return JsonResponse({
        "status": result.status
    })

def resultview(request, id):
    result = AsyncResult(id)
    result_set = {
        "id": id,
        "status": result.status, 
        "result": result.result
    }
    return JsonResponse(result_set, status=200)

