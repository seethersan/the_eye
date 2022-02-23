from django.urls import path
from api.views import ApplicationViewSet, EventViewSet, SessionViewSet

urlpatterns = [
    path('applications', ApplicationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('appications/<int:pk>', ApplicationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('events', EventViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('events/<int:pk>', EventViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('sessions', SessionViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('sessions/<str:pk>', SessionViewSet.as_view({
        'get': 'list_events',
        'put': 'update',
        'delete': 'destroy'
    })),
]