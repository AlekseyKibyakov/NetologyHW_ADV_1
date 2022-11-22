from application.salary import calculate_salary as get_salary
from application.db.people import get_employees
from datetime import date
from jinja2 import Environment

if __name__ == '__main__':
    env = Environment(extensions=['jinja2_time.TimeExtension'])
    get_salary(11)
    get_employees(2)
    
    print(f'{date.today()}\n') #вывод текущей даты через datetime
    
    print(env.from_string("{% now 'local' %}").render()) #вывод текущей даты с помощью jinja2