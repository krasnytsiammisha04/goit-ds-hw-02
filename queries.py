import sqlite3

def execute_query(sql):
    with sqlite3.connect('task_manager.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql_task_by_user = "SELECT * FROM tasks WHERE user_id = 1"
print(execute_query(sql_task_by_user))

