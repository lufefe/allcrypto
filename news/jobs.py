from apscheduler.schedulers.background import BackgroundScheduler
from .BackgroundClass import BackgroundClass


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(BackgroundClass.update_db, 'interval', minutes=1)
    scheduler.start()