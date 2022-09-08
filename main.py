import os
import argparse
import subprocess
from  listener.event_handler import CeleryEventsHandler
from celery import Celery

app = Celery("analyzer", 
    broker = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0"),
    backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0"),
    include= ["tasks"]
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="celery", choices=["celery", "listener"])

    args = parser.parse_args()

    if args.mode == "celery":
        subprocess.call("celery -A main.app worker -E --loglevel=info", shell=True)
    elif args.mode == "listener":
        print("Start listening....")
        events_handler = CeleryEventsHandler(app, True)
        events_handler.start_listening()
    else:
        print("Invalid command!")
        exit()
    