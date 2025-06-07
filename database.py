import sqlite3
import bcrypt

# Initialize the database
def initialize_db():
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        # Create the users table
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL UNIQUE,
                        password BLOB NOT NULL
                    )''')
        # Create the tasks table
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER NOT NULL,
                        day TEXT NOT NULL,
                        subject TEXT NOT NULL,
                        start_time TEXT NOT NULL,
                        details TEXT NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )''')
        conn.commit()

def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def validate_login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    record = c.fetchone()
    conn.close()
    if record and bcrypt.checkpw(password.encode('utf-8'), record[0]):
        return True
    return False
def add_task(user_id, day, subject, start_time, details):
    try:
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO tasks (user_id, day, subject, start_time, details) VALUES (?, ?, ?, ?, ?)',
                      (user_id, day, subject, start_time, details))
            conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def get_tasks(user_id):
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('SELECT day, subject, start_time, details FROM tasks WHERE user_id = ?', (user_id,))
        tasks = c.fetchall()
    return tasks

def get_id(username):
    with sqlite3.connect('users.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT id FROM users WHERE username = ?', (username,))
        user_id = cur.fetchone()
    return user_id[0] if user_id else None
def get_task_by_id(task_id):
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('SELECT day, subject, start_time, details FROM tasks WHERE id = ?', (task_id,))
        task = c.fetchone()
    return task

def update_task(task_id, day, subject, start_time, details):
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('UPDATE tasks SET day = ?, subject = ?, start_time = ?, details = ? WHERE id = ?',
                  (day, subject, start_time, details, task_id))
        conn.commit()
def delete_task(task_id):
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()

def get_tasks(user_id):
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('SELECT id, day, subject, start_time, details FROM tasks WHERE user_id = ?', (user_id,))
        tasks = c.fetchall()
    return tasks
