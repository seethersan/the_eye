from rest_framework import serializers
from api.models import Application, Session, Event
from datetime import datetime
from django.utils import timezone
from collections import Counter

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

    def validate(self, data):
        errors = {}

        user = self.context.get("request").user
        if data['application'].user != user:
            errors['application'] = 'this application is not authorized to the current user'
        if data['timestamp'] > timezone.make_aware(datetime.now()):
            errors['timestamp'] = 'timestamp doesnt not allow future dates'
        if data['category'] == 'page interaction':
            if data['name'] == 'pageview':
                if not Counter(data['data'].keys()) == Counter(["host", "path"]):
                    errors['data'] = "event payload for {} {} must have only host and path keys".format(data['category'], data['name'])
            elif data['name'] == 'cta click':
                if not Counter(data['data'].keys()) == Counter(["host", "path", "element"]):
                    errors['data'] = "event payload for {} {} must have only host, path and element keys".format(data['category'], data['name'])
        elif data['category'] == 'form interaction':
            if data['name'] == 'submit':
                if not Counter(data['data'].keys()) == Counter(["host", "path", "form"]):
                    errors['data'] = "event payload for {} {} must have only host, path and element keys".format(data['category'], data['name'])

        if errors:
            raise serializers.ValidationError(errors)
        
        return data