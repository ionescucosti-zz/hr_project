import json
import os
import sqlite3
from datetime import datetime

from hr_project.settings import BASE_DIR


def load_data():
    with open("MOCK_DATA.json", "r") as f:
        data = json.load(f)
        to_db = [(i['id'], i['first_name'], i['last_name'], i['email'], i['gender'],
                  datetime.strptime(i['date_of_birth'].replace('/', ''), "%d%m%Y").date(),
                  i['industry'], i['salary'], i['years_of_experience']) for i in data]
        con = sqlite3.connect(os.path.join(BASE_DIR, 'db.sqlite3'))
        cur = con.cursor()
        cur.executemany("INSERT INTO hr_app_employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
        con.commit()
        con.close()


if __name__ == "__main__":
    load_data()