from project import create_app
from celery import Celery
from event_handler import CeleryEventsHandler
app = create_app()

celery = app.celery_app

if __name__ == "__main__":
  events_handler = CeleryEventsHandler(celery, True)
  events_handler.start_listening()
