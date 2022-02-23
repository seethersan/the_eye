from rest_framework import serializers
from api.models import Application, Session, Event

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    application_id = serializers.PrimaryKeyRelatedField(
        source='application',
        queryset=Application.objects.all()
    )
    session_id = serializers.PrimaryKeyRelatedField(
        source='session',
        queryset=Session.objects.all()
    )

    application = ApplicationSerializer(read_only=True)
    session = SessionSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['session', 'session_id', 'application', 'application_id', 'category', 'name', 'data', 'timestamp']