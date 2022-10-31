from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name='apiOverview' ),
    path('project-list/',views.ShowAll,name='project-list'),
    path('project-detail/<int:pk>',views.ViewProject,name='project-detail'),
    path('create/',views.CreateProject,name='project-create'),
    path('update/<int:pk>',views.editProject,name='project-edit/update'),
    path('delete/<int:pk>',views.deleteProject,name='project-delete'),
]