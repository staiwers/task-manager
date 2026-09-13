from sqlite3 import *


def create_task(title, description) -> None:
    connection = connect('task_menager.db')
    cursor = connection.cursor()

    cursor.execute(
        'INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    
    connection.commit()
    connection.close()


def read_tasks(id) -> list:
    connection = connect('task_menager.db')
    cursor = connection.cursor()

    if id == '':
        cursor.execute('SELECT id, title, description, status, date_create FROM tasks')
    else:
        cursor.execute('SELECT id, title, description, status, date_create FROM tasks WHERE id = ?', (id))

    list_tasks = cursor.fetchall()
    connection.close()
    return list_tasks


def update_task(id, user_text) -> None:
    id = int(id)
    connection = connect('task_menager.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (user_text, id))

    connection.commit()
    connection.close()


def delete_task(id) -> None:
    connection = connect('task_menager.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = ?', (id))

    connection.commit()
    connection.close()