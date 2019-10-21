import sqlite3
import json

database = './todo.db'


def add_task(request, user_id):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute('insert into tasks(user_id, task, isDone, due) values(?,?,?,?)',
                  (user_id, request["task"], request["isDone"], request["due"]))
        conn.commit()
        return request
    except Exception as e:
        print('Error: ', e)
        return None
    finally:
        conn.close()


def get_all_tasks(user_id):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        result = c.execute('select * from tasks where user_id=?', (user_id))
        tasks = [dict(zip([key[0] for key in c.description], row))
                 for row in result]
        return tasks
    except Exception as e:
        print('Error: ', e)
        return None
    finally:
        conn.close()


def get_task(user_id, task_id):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        result = c.execute('select task, isDone, due from tasks where user_id=? and task_id=?',
                           (user_id, task_id))
        task = [dict(zip([key[0] for key in c.description], row))
                for row in result]
        return task
    except Exception as e:
        print('Error: ', e)
        return None
    finally:
        conn.close()


def update_task(request, user_id, task_id):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute('update tasks set task=?, isDone=?, due=?  where user_id=? and task_id=?',
                  (request["task"], request["isDone"], request["due"], user_id, task_id))
        conn.commit()
        if(c.rowcount > 0):
            return request
        else:
            return None
    except Exception as e:
        print('Error: ', e)
        return None
    finally:
        conn.close()


def delete_task(user_id, task_id):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute('delete from tasks where user_id=? and task_id=?',
                  (user_id, task_id))
        conn.commit()
    except Exception as e:
        print('Error: ', e)
        return None
    finally:
        conn.close()
