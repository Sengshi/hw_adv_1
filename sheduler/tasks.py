from apscheduler.schedulers.background import BlockingScheduler
from .sheduler import jump


def start():
    scheduler = BlockingScheduler()
    scheduler.add_job(jump, 'interval', seconds=5)
    print(f'Я поскакал')
    scheduler.start()
