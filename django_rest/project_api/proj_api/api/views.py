from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import ProjectSerializer,ClientSerializer
from .models import project,client

# Create your views here.

@api_view()
@permission_classes([AllowAny])
def apiOverview(request):
    api_urls={
         'List': '/project-list/',
         'Detail View': '/project-detail/<int:id>/',
         'Create': '/create/',
         'Update': '/update/<int:id>/',
         'Delete': '/delete/<int:id>/',
    }

    return Response(api_urls);

class projectviewset(viewsets.ModelViewSet):
    serializer_class= ProjectSerializer

    def get_queryset(self):
        projects = project.objects.all()
        return projects

class clientviewset(viewsets.ModelViewSet):
    serializer_class= ClientSerializer

    def get_queryset(self):
        clients = client.objects.all()
        return clients

@api_view(['GET'])
def ShowAll(request):
    projects = project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProject(request, pk):
    projects = project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProject(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def editProject(request, pk):
    projects = project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=projects, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def deleteProject(request, pk):
    projects = project.objects.get(id=pk)
    projects.delete()

    return Response('Items delete successfully!')

