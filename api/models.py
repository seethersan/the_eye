from django.conf import settings
from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
class Session(models.Model):
    id = models.UUIDField(primary_key=True)

class Event(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    data = models.JSONField()
    timestamp = models.DateTimeField()