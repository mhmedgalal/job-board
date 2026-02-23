from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .filter import JobFilter
from .models import Apply, Job
from .serializers import ApplySerializer, JobSerializer


class JobPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def job_list(request):
    if request.method == "GET":
        filter_set = JobFilter(
            request.GET,
            queryset=Job.objects.select_related("category", "owner").order_by("-published_at"),
        )
        paginator = JobPagination()
        jobs = paginator.paginate_queryset(filter_set.qs, request)
        serializer = JobSerializer(jobs, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def job_detail(request, pk):
    job = get_object_or_404(Job, id=pk)

    if request.method == "GET":
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if job.owner != request.user:
        return Response(
            {"detail": "You are not allowed to update or delete this job"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "PUT":
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    job.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def apply(request):
    if request.method == "POST":
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    applies = Apply.objects.filter(user=request.user).select_related("job")
    serializer = ApplySerializer(applies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def job_applies(request, pk):
    job = get_object_or_404(Job, id=pk)

    if job.owner != request.user:
        return Response(
            {"detail": "You are not allowed to view applications for this job"},
            status=status.HTTP_403_FORBIDDEN,
        )

    applies = Apply.objects.filter(job=job).select_related("user")
    serializer = ApplySerializer(applies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
