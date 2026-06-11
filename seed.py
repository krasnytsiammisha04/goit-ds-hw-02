import sqlite3
import faker
from random import randint, choice


def seed_db():
    fake = faker.Faker()
    users = [(fake.name(), fake.unique.email()) for _ in range(10)]
    statuses = [('new',), ('in progress',), ('completed',)]

    with sqlite3.connect('task_manager.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO users(fullname, email) VALUES(?, ?)", users)
        cur.executemany("INSERT INTO status(name) VALUES(?)", statuses)


        tasks = []
        for _ in range(20):
            tasks.append((fake.sentence(), fake.text(), randint(1, 3), randint(1, 10)))

        cur.executemany("INSERT INTO tasks(title, description, status_id, user_id) VALUES(?, ?, ?, ?)", tasks)
        con.commit()


if __name__ == "__main__":
    seed_db()