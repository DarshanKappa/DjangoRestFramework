from django.shortcuts import render
from rest_framework.views import APIView
from CRUD.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class StudentAPI(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)

        return Response(serializer.data)

    def post(self, request, pk=None, format=None):
        data = request.data.dict()

        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            res = {'msg':'Data has Created'}
            serializer.save()
            return Response(res, status=status.HTTP_201_CREATED)

        return Response({'error':'something wrong here'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        data = request.data.dict()
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu ,data=data , partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'Data has Updated'})

        return Response({'error':'something wrong here'}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        data = request.data.dict()
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu ,data=data , partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'Data has Updated'})

        return Response({'error':'something wrong here'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = request.data.dict()
        stu = Student.objects.get(id=data.get('id'))
        
        if stu:
            stu.delete()
            return Response({'msg':'Data has Deleted'})

        return Response({'error':'something wrong here'}, status=status.HTTP_400_BAD_REQUEST)
