from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from sheduler import tasks


if __name__ == '__main__':
    print(f'Текущая дата: {datetime.now().strftime("%d-%m-%Y")}, время: {datetime.now().strftime("%H:%M:%S")}')
    calculate_salary()
    get_employees()
    tasks.start()
