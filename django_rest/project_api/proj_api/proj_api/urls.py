
from django.contrib import admin
from django.urls import path,include
from api import views

from rest_framework.routers import DefaultRouter
#creating router object
router=DefaultRouter()
#register
router.register('project',views.projectviewset,basename='project')
router.register('client',views.clientviewset,basename='client')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api.urls'))
]
