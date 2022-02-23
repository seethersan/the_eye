from celery import shared_task
from celery.utils.log import get_task_logger
from api.models import Event

logger = get_task_logger(__name__)

@shared_task
def create_event(event):
    event = Event.objects.create(**event)
    try:
        event.save()
    except Exception as e:
        logger.error("Error while processing Event: {}".format(e))
    else:
        logger.info("Event {} created successfully".format(event.id))