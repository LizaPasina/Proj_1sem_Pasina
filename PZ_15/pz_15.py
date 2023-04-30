import sqlite3 as sq
from info_data import info_tov, info_mag, info_zayv, info_kol, info_sostav

with sq.connect('optovaya_baza.db') as con:
    con.execute('PRAGMA foreign_keys = ON')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tovari(
       id INTEGER PRIMARY KEY,
       name VARCHAR NOT NULL,
       description VARCHAR NOT NULL,
       unit VARCHAR
       )""")

with sq.connect('optovaya_baza.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS magazini(
       id INTEGER PRIMARY KEY,
       name VARCHAR NOT NULL,
       adress VARCHAR,
       phone VARCHAR NOT NULL
       )""")

with sq.connect('optovaya_baza.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS zayavki_magazinov(
       id INTEGER PRIMARY KEY,
       magazini_id INTEGER,
       data DATE,
       FOREIGN KEY (magazini_id) REFERENCES magazini(id) ON DELETE CASCADE ON UPDATE CASCADE
       )""")

with sq.connect('optovaya_baza.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS kolichestvo(
       id INTEGER PRIMARY KEY,
       tovari_id INTEGER,
       kolvo INTEGER,
       FOREIGN KEY (tovari_id) REFERENCES tovari(id) ON DELETE CASCADE ON UPDATE CASCADE
       )""")

with sq.connect('optovaya_baza.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sostav(
       id INTEGER PRIMARY KEY,
       id_zayavki INTEGER,
       tovari_id INTEGER,
       kolvo INTEGER,
       FOREIGN KEY (id_zayavki) REFERENCES zayavki_magazinov(id) ON DELETE CASCADE ON UPDATE CASCADE,
       FOREIGN KEY (tovari_id) REFERENCES tovari(id) ON DELETE CASCADE ON UPDATE CASCADE
       )""")

# with sq.connect('optovaya_baza.db') as con:
#       cur = con.cursor()


# with sq.connect('optovaya_baza.db') as con:
#       cur.executemany("INSERT INTO tovari VALUES (?,?,?,?)", info_tov)
#       cur = con.cursor()
#       cur.executemany("INSERT INTO magazini VALUES (?,?,?,?)", info_mag)


# with sq.connect('optovaya_baza.db') as con:
#       cur = con.cursor()
#       cur.executemany("INSERT INTO zayavki_magazinov VALUES (?,?,?)", info_zayv)


# with sq.connect('optovaya_baza.db') as con:
#       cur = con.cursor()
#       cur.executemany("INSERT INTO kolichestvo VALUES (?,?,?)", info_kol)


# with sq.connect('optovaya_baza.db') as con:
#       cur = con.cursor()
#       cur.executemany("INSERT INTO sostav VALUES (?,?,?,?)", info_sostav)


# 1
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, description FROM tovari")
#     res = cur.fetchall()
# print(res)


# 2
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, adress FROM magazini")
#     res = cur.fetchall()
# print(res)


# 3
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT magazini.name, zayavki_magazinov.data FROM magazini INNER JOIN zayavki_magazinov ON magazini.id = zayavki_magazinov.id")
#     res = cur.fetchall()
# print(res)


# 4
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, kolvo FROM tovari, kolichestvo WHERE tovari.id=tovari_id")
#     res = cur.fetchall()
# print(res)


# 5
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, kolvo FROM tovari, kolichestvo WHERE tovari.id=tovari_id ORDER BY kolichestvo.kolvo DESC")
#     res = cur.fetchall()
# print(res)


# 6
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id_zayavki, name FROM sostav, tovari WHERE tovari_id=tovari.id")
#     res = cur.fetchall()
# print(res)


# 7
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, kolvo FROM tovari, kolichestvo WHERE tovari.id=tovari_id AND kolvo < 40")
#     res = cur.fetchall()
# print(res)


# 8
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT id, data FROM zayavki_magazinov WHERE data >= '2023-03-01' AND data <= '2023-06-01'")
#     res = cur.fetchall()
# print(res)


# 9
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("SELECT name, kolvo FROM magazini JOIN sostav ON magazini.id=sostav.id WHERE sostav.kolvo < 50")
#     res = cur.fetchall()
# print(res)


# Обновление 1
# with sq.connect('optovaya_baza.db') as con:
#      cur = con.cursor()
#      cur.execute("UPDATE kolichestvo SET kolvo=24 WHERE tovari_id=7")


# 2 объединили 2 и 3 задание обновляем дату заявки по id
# with sq.connect('optovaya_baza.db') as con:
#      cur = con.cursor()
#      cur.execute("UPDATE zayavki_magazinov SET data='2023-09-22' WHERE id=22")


# 3
# with sq.connect('optovaya_baza.db') as con:
#      cur = con.cursor()
#      cur.execute("UPDATE magazini SET adress='ул. Шишкина 34/43' WHERE id=33")


# 4
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE zayavki_magazinov SET data='2023-04-04' WHERE magazini_id=99")


# 5
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE kolichestvo SET kolvo=kolvo+23 WHERE tovari_id<=4")


# 6
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE tovari SET description='коровье' WHERE name LIKE 'молоко'")
#     cur.execute("UPDATE kolichestvo SET kolvo=42 WHERE id=5")


# 7
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE kolichestvo SET kolvo=kolvo+5 WHERE tovari_id=2")


# 8
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE kolichestvo SET kolvo=kolvo+5 WHERE tovari_id=2")


# 9
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("UPDATE kolichestvo SET kolvo=kolvo+10 WHERE tovari_id=5")


# 1 удаление
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM sostav WHERE id_zayavki=88")
#     cur.execute("DELETE FROM zayavki_magazinov WHERE id=88")


# 2
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM kolichestvo WHERE tovari_id IN (SELECT id_zayavki FROM sostav WHERE id_zayavki=0)")


# 3
# with sq.connect('optovaya_baza.db') as con:
#      cur = con.cursor()
#      cur.execute("DELETE FROM zayavki_magazinov WHERE id IN (SELECT id FROM magazini WHERE adress LIKE 'ул. Мазилина%')")


# 5
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM magazini WHERE id IN (SELECT id FROM zayavki_magazinov WHERE data < '2023-04-22')")


# 6
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM tovari WHERE id IN (SELECT id FROM sostav WHERE id_zayavki=0)")


# 7
# with sq.connect('optovaya_baza.db') as con:
#     cur = con.cursor()
#     cur.execute("DELETE FROM kolichestvo WHERE id IN (SELECT id FROM sostav WHERE id_zayavki=0)")

