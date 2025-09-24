from rest_framework import generics  
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets   
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from .models import Job, Category, Apply
from .serializers import JobSerializer, CategorySerializer, ApplySerializer
from rest_framework import status
from .filter import JobFilter
from rest_framework.pagination import PageNumberPagination


class JobPagination(PageNumberPagination):
    page_size = 5               
    page_size_query_param = 'page_size'  
    max_page_size = 50          


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def job_list(request):
    if request.method == 'GET':
        # فلترة
        filter_set = JobFilter(request.GET, queryset=Job.objects.all().order_by('id'))
        count = filter_set.qs.count()

        # Pagination
        paginator = JobPagination()
        jobs = paginator.paginate_queryset(filter_set.qs, request)

        # Serialize
        serializer = JobSerializer(jobs, many=True)
        return paginator.get_paginated_response({
            "count": count,
            "per_page": paginator.get_page_size(request),
            "jobs": serializer.data
        })

    elif request.method == 'POST':
        if not request.user or not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def job_detail (request,pk):
    job = get_object_or_404(Job,id=pk)
    if request.method in ['PUT', 'DELETE']:
        if job.owner != request.user:
            return Response({"detail":"You are not allowed to update or delete this job"},
                            status=status.HTTP_403_FORBIDDEN)
        
        
    if request.method == 'PUT':
        data = request.data
        serializer = JobSerializer(job,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                           status=status.HTTP_200_OK)
        else:
           return Response(serializer.errors,
                           status=status.HTTP_400_BAD_REQUEST)
        




    elif  request.method == 'GET':
        job = get_object_or_404(Job,id=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data,
                           status=status.HTTP_200_OK)
    



    elif request.method == 'DELETE':
        job = get_object_or_404(Job,id=pk)
        job.delete()
        return Response({"details" : "delete is done"},
                        status=status.HTTP_204_NO_CONTENT)
    



@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def apply(request):
    if request.method == 'POST':
        data = request.data
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"details" : "save is done"}
                            ,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        


    elif request.method == 'GET':
        applies = Apply.objects.filter(user=request.user)
        serializer = ApplySerializer(applies,many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
    


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def job_applies(request, pk):
    job = get_object_or_404(Job, id=pk)

    # نتاكد إن اللي طالب البيانات هو صاحب الوظيفة
    if job.owner != request.user:
        return Response({"detail": "You are not allowed to view applications for this job"},
                        status=status.HTTP_403_FORBIDDEN)

    applies = Apply.objects.filter(job=job)
    serializer = ApplySerializer(applies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

