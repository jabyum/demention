import sqlite3
from datetime import datetime
connection = sqlite3.connect("dbotbase.db")
sql = connection.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS bot_users (tg_id INTEGER, name TEXT, category TEXT, "
            "phone_number TEXT, reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS vacancies (vac_id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER, disease TEXT, age TEXT, "
            "salary TEXT, phone_number TEXT, vac_reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOt EXISTS admins (admin_id INTEGER, rank INTEGER, admin_reg_date DATETIME);")
def register_user(user_id, name, phone_number, category):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO bot_users (tg_id, name, phone_number, category, reg_date) "
                "VALUES (?, ?, ?, ?, ?);", (user_id, name, phone_number, category, datetime.now()))
    connection.commit()
def add_admin(admin_id, rank):
    connection = sqlite3.connect('dbotbase.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO admins (admin_id, rank, admin_reg_date)'
                'VALUES (?, ?, ?);', (admin_id, rank, datetime.now()))
    connection.commit()
def check_vac(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT tg_id FROM vacancies WHERE tg_id=?;", (user_id, ))
    if checker.fetchone():
        return True
    else:
        return False
def add_vacancies(user_id, disease, age, salary, phone_number):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO vacancies (tg_id, disease, age, salary, phone_number, vac_reg_date) "
                "VALUES (?, ?, ?, ?, ?, ?);", (user_id, disease, age, salary, phone_number, datetime.now()))
    connection.commit()
def delete_vacancies(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM vacancies WHERE tg_id=?;", (user_id,))
    connection.commit()
def check_user(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT tg_id FROM bot_users WHERE tg_id=?;", (user_id, ))
    if checker.fetchone():
        return True
    else:
        return False
def delete_exact_vac(vac_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM vacancies WHERE vac_id=?;"), (vac_id, )
    connection.commit()
def get_user_name_and_number(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    exact_user = sql.execute("SELECT name, phone_number FROM bot_users WHERE tg_id=?;", (user_id, )).fetchone()
    return exact_user
def get_user_number(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    exact_user = sql.execute("SELECT phone_number FROM bot_users WHERE tg_id=?;", (user_id, )).fetchone()
    return exact_user
def get_user_category(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    exact_user = sql.execute("SELECT category FROM bot_users WHERE tg_id=?;", (user_id, )).fetchone()
    return exact_user
def get_vacancies():
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    vacancies = sql.execute("SELECT vac_id, disease, age, salary, phone_number FROM vacancies;").fetchall()
    return vacancies
def check_admin(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT admin_id FROM admins WHERE admin_id=?;", (user_id, ))
    if checker.fetchone():
        return True
    else:
        return False
def check_admin_rank(user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT rank FROM admins WHERE admin_id=?;", (user_id, ))
    if checker.fetchone():
        return checker.fetchone()
    else:
        return False
def mailing(targets):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    select_target_base = sql.execute("SELECT tg_id FROM bot_users WHERE category=?;", (targets, )).fetchall()
    select_target = [i[0] for i in select_target_base]
    return select_target
def mailing_all():
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    all_targets = sql.execute("SELECT tg_id FROM bot_users;",).fetchall()
    return all_targets
def update_category(new_category, user_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    sql.execute("UPDATE bot_users SET category=? WHERE tg_id=?;", (new_category, user_id))
    connection.commit()
def delete_admin(admin_id):
    connection = sqlite3.connect("dbotbase.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM admins WHERE admin_id=?;", (admin_id, ))
    connection.commit()