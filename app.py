from start_logo import print_start_logo
from init_db import init_db
from CRUD import create_task, read_tasks, update_task, delete_task

from sqlite3 import *


print_start_logo()

init_db()

# MENU
again = True
while again == True:
    print("'c'-create , 'r'-read, 'u'-update, 'd'-delete, 'e'-exit")

    user_data = input().lower()

    if user_data == 'c':
        create_task(input('print title >>>: '), input('print description (or nothing) >>>: '))
        print(*read_tasks(''), sep = '\n')

    elif user_data == 'r':
        print(*read_tasks(input('print id >>>: ')), sep = '\n')

    elif user_data == 'u':
        update_task(input('print id >>>: '), input('print text for status >>> :'))
        print(*read_tasks(''), sep = '\n')

    elif user_data == 'd':
        delete_task(input('print id >>>: '))
        print(*read_tasks(''), sep = '\n')
    elif user_data in ('e', 'q'):
        again = False