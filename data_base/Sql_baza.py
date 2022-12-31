import sqlite3
import pathlib
import sys

def get_script_dir():
    abs_path = pathlib.Path(sys.argv[0]).parent
    return abs_path


def open_sql():
    global bd
    global cur
    bd = sqlite3.connect(get_script_dir() / "data_base/baza.db")
    cur = bd.cursor()


def close_sql():
    cur.close()
    bd.close()

def chek_user_in_bd(id_user, user_name):    # Проверяет есть ли пользователь в базе
    open_sql()
    try:
        cur.execute("SELECT id FROM users WHERE id={}".format(str(id_user)))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO users (id_user,name) VALUES (?,?)", (id_user, user_name))
        else:
            cur.execute(f'UPDATE users SET data_visit=date("now") WHERE id={id_user}')
    except sqlite3.DatabaseError as err:
        print("Ошибка: chek_user_in_bd", err)
    else:
        bd.commit()
    close_sql()
# def get_batton_area():  # Возвращает список районов
#     mas = []
#     open_sql()
#     try:
#         cur.execute("select name from area")
#         for item in cur.fetchall():
#             for i in item:
#                 mas.append(i)
#     except sqlite3.DatabaseError as err:
#         print("Ошибка: get_batton_area", err)
#     else:
#         return mas
#     close_sql()
#
#

#
#
# def get_profil(id_user):  # передает данные о профиле по его id
#     open_sql()
#     try:
#         cur.execute("SELECT * FROM users WHERE id = {}".format(id_user))
#         getaccess = cur.fetchone()
#         if getaccess[4] == 0:
#             accessname = 'Пользователь'
#         elif getaccess[4] == 1:
#             accessname = 'Администратор'
#         elif getaccess[4] == 777:
#             accessname = 'Разработчик'
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: ', err)
#     else:
#         return accessname, getaccess
#     close_sql()
#
#
# def get_product():  # передает асортименрт товаров
#     open_sql()
#     try:
#         cur.execute("select * from products")
#         products = cur.fetchall()
#     except sqlite3.DatabaseError as err:
#         print("Ошибка get_product:", err)
#     else:
#         return products
#     close_sql()
#
#
# def get_access(id_user):  # передает данные о профиле по его id
#     open_sql()
#     try:
#         cur.execute("SELECT access FROM users WHERE id = {}".format(id_user))
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: get_access', err)
#     else:
#         return cur.fetchall()[0]
#     close_sql()
#
#
# def give_access(id_user):  # выдает признак админа в бд
#     open_sql()
#     try:
#         cur.execute(f"UPDATE users SET access='777' WHERE id={id_user}")
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: get_access', err)
#     else:
#         bd.commit()
#     close_sql()
#
#
# def get_payment_not_chek(id_user):  # Возвращает пользователю все не оплаченные заказы
#     open_sql()
#     try:
#         cur.execute(
#             "SELECT A.id,A.name, B.count, B.sum FROM paymant as B JOIN products as A ON A.id=B.id_product WHERE B.id_man={} AND B.flag = {}".format(
#                 id_user, 0))
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: get_payment_not_chek', err)
#     else:
#         return cur.fetchall()
#         bd.commit()
#     close_sql()
#
#
# def buy_tovar_for_user(id_user):  # Возвращает количество ранее купленных заказов
#     open_sql()
#     try:
#         cur.execute(f"SELECT COUNT(*) FROM paymant WHERE id=(?) and flag<>(?)", (id_user, 0))
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: buy_tovar_for_user', err)
#     else:
#         return cur.fetchone()[0]
#         bd.commit()
#     close_sql()
#
#
# def get_list_last_products(id_user):  # Возвращает все оплаченные товары
#     open_sql()
#     try:
#         cur.execute(
#             f"SELECT A.name, B.count, B.sum FROM paymant as B JOIN products as A on b.id=A.id WHERE B.id_man=(?) and flag<>(?)",
#             (id_user, 1))
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: get_list_last_products', err)
#     else:
#         return cur.fetchall()
#         bd.commit()
#     close_sql()
#
#
# def insert_product_karz(id_user, area, id_prod, count):
#     open_sql()
#     try:
#         cur.execute(f'SELECT price from products where id={id_prod}')
#         summa = cur.fetchone()[0] * count
#         cur.execute(f'select id from paymant WHERE id_man={id_user} and id_product={id_prod}')
#         if cur.fetchone():
#             cur.execute(
#                 f"UPDATE paymant SET sum=sum+{summa},count=count+{count} WHERE id_man={id_user} AND id_product={id_prod}")
#         else:
#             cur.execute(f"INSERT INTO paymant(id_product,id_man,count,sum) VALUES(?,?,?,?)",
#                         (id_prod, id_user, count, summa))
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: insert_product_karz', err)
#     else:
#         bd.commit()
#     close_sql()
#
#
# def drop_product_from_basket(user_id, id_prod):  # удаляет товар из корзины
#     open_sql()
#     try:
#         cur.execute(f'DELETE FROM paymant WHERE id_man={user_id} and id_product={id_prod} and flag=0')
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: drop_product_from_basket', err)
#     else:
#         bd.commit()
#     close_sql()
#
#
# def add_product_in_db(arr):  # Добавлет новые товары в базу
#     open_sql()
#     try:
#         cur.execute(f"INSERT INTO products (name,price,description) VALUES (?,?,?)", tuple(arr))
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: add_product_in_db', err)
#     else:
#         bd.commit()
#     close_sql()
#
#
# def name_product(id_prod):  # возвращает имя товара по его id
#     open_sql()
#     try:
#         cur.execute(f"SELECT name FROM products WHERE id={id_prod}")
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: name_product', err)
#     else:
#         return cur.fetchone()[0]
#         bd.commit()
#     close_sql()
#
#
# def select_users():  # просмотр всех пользователей
#     open_sql()
#     try:
#         cur.execute('SELECT name, data_visit from users')
#     except sqlite3.DatabaseError as err:
#         print('Ошибка: select_users', err)
#     else:
#         return list(cur.fetchall())
#         bd.commit()
#     close_sql()