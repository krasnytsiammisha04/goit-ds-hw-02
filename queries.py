import sqlite3

def execute_query(sql):
    with sqlite3.connect('task_manager.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# 1. Отримати всі завдання певного користувача
q1 = "SELECT * FROM tasks WHERE user_id = 1"

# 2. Вибрати завдання за певним статусом
q2 = "SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new')"

# 3. Оновити статус конкретного завдання
q3 = "UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1"

# 4. Отримати список користувачів, які не мають жодного завдання
q4 = "SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)"

# 5. Додати нове завдання для конкретного користувача
q5 = "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Нове завдання', 'Опис', 1, 1)"

# 6. Отримати всі завдання, які ще не завершено
q6 = "SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')"

# 7. Видалити конкретне завдання
q7 = "DELETE FROM tasks WHERE id = 1"

# 8. Знайти користувачів з певною електронною поштою
q8 = "SELECT * FROM users WHERE email LIKE '%@gmail.com'"

# 9. Оновити ім'я користувача
q9 = "UPDATE users SET fullname = 'Mykhailo Krasnytsia' WHERE id = 1"

# 10. Отримати кількість завдань для кожного статусу
q10 = "SELECT s.name, COUNT(t.id) FROM status s LEFT JOIN tasks t ON s.id = t.status_id GROUP BY s.name"

# 11. Отримати завдання, які призначені користувачам з певною доменною частиною
q11 = "SELECT t.* FROM tasks t JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%@example.com'"

# 12. Отримати список завдань, що не мають опису
q12 = "SELECT * FROM tasks WHERE description IS NULL OR description = ''"

# 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
q13 = "SELECT u.fullname, t.title FROM users u INNER JOIN tasks t ON u.id = t.user_id WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress')"

# 14. Отримати користувачів та кількість їхніх завдань
q14 = "SELECT u.fullname, COUNT(t.id) FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.id"

# Ви можете додати вивід результатів для перевірки, наприклад:
# print(execute_query(q10))