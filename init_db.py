from sqlite3 import *

def init_db() -> None:
    connection = connect('task_menager.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'new',
    date_create TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ''')

    connection.commit()
    connection.close()