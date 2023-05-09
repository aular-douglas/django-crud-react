from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views

routers = routers.DefaultRouter()
routers.register('tasks', views.TaskView, 'tasks' )


urlpatterns = [
    path("api/v1/", include(routers.urls)),
    path('docs/', include_docs_urls(title="Tasks API"))
]
