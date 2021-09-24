from functools import partial
from rest_framework import serializers
from rest_framework.decorators import api_view
from CRUD.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response



@api_view(['GET','POST','PUT','DELETE'])
def stu_api(request):

    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data.dict()

        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            res = {'msg':'Data has Created'}
            serializer.save()
            return Response(res)

        return Response({'error':'something wrong here'})


    if request.method == 'PUT':
        data = request.data.dict()
        stu = Student.objects.get(id=data.get('id'))
        serializer = StudentSerializer(stu ,data=data , partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'Data has Updated'})

        return Response({'error':'something wrong here'})

    if request.method == 'DELETE':
        data = request.data.dict()
        stu = Student.objects.get(id=data.get('id'))
        
        if stu:
            stu.delete()
            return Response({'msg':'Data has Deleted'})

        return Response({'error':'something wrong here'})
        

