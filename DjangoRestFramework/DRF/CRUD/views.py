from functools import partial
import json
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerialize
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def studentDetail(request, pk):

    stu = Student.objects.get(id=pk)
    serialize_data = StudentSerialize(stu)

    return JsonResponse({'data':serialize_data.data})

@csrf_exempt
def crud_methods(request):

    if request.method == "GET":

        stu = Student.objects.all()
        serialize_data = StudentSerialize(stu, many=True)

        return JsonResponse({'data':serialize_data.data})
  

    if request.method == "POST":
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # print(stream)
        stream = request.POST.dict()
        print(stream)
        # python_data = JSONParser().parse(stream)
        # print(python_data)

        serializer = StudentSerialize(data=stream)

        print('in the create student')
        if serializer.is_valid():
            print('in the create before')
            serializer.save()
            res = {'msg':'Data Created'}

            # json_data = JSONRenderer().render(res)
            return JsonResponse(res)
        else:
            print('------------------------')
            return JsonResponse({'error':'sometning wrong here'})

    if request.method == 'PUT':
        print('-----------OK---------------')
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        print(python_data)
        # print(request.PUT.get('id'))

        id = python_data.pop('id')
        print(id)
        print(python_data)
        stu = Student.objects.get(id=id)
        serializer = StudentSerialize(stu, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data have updated'}

            return JsonResponse(res)
        else:
            return JsonResponse({'error':'something wrong here'})


    if request.method == "DELETE":

        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        stu = Student.objects.get(id=python_data.get('id'))
        stu.delete()
        res = {'msg':'Data Deleted'}
        return JsonResponse(res)
