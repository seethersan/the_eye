from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Application, Event, Session
from api.serializers import ApplicationSerializer, EventSerializer, SessionSerializer

class ApplicationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def create(self, request):
        request.data['user'] = self.request.user.id
        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        application = Application.objects.get(id=pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

    def update(self, request, pk=None):
        application = Application.objects.get(id=pk)
        request.data['user'] = self.request.user.id
        serializer = ApplicationSerializer(instance=application, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        application = Application.objects.get(id=pk)
        application.delete()
        return Response(satus=status.HTTP_204_NO_CONTENT)

class SessionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def list_events(self, request, pk=None):
        events = Event.objects.filter(session_id=pk).order_by('-timestamp')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        session = Session.objects.get(id=pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def update(self, request, pk=None):
        session = Session.objects.get(id=pk)
        serializer = SessionSerializer(instance=session, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        session = Session.objects.get(id=pk)
        session.delete()
        return Response(satus=status.HTTP_204_NO_CONTENT)