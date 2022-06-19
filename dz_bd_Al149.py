# Создайте новую Базу данных. Поля: id, 2 целочисленных поля.
# Целочисленные поля заполняются рандомно от 0 до 9.
# Посчитать среднее арифметическое всех элементов без учета id.
# Если среднее арифметическое больше количества записей в БД, то удалить четвертую запись БД.
#
import sqlite3
import random

# создать базу данных
newbase = sqlite3.connect("sredarifmet.db")

# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = newbase.cursor()
# создадим таблицу с двумя целочисленными колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')

# заполняем таблицу данными
a = str([random.randint(0, 9) for k in range(1)])
b = str([random.randint(0, 9) for l in range(1)])
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (a, b))
newbase.commit() #сохраняем изменения
cursor.execute('''SELECT col_1, col_2 FROM tab_1''')
s = cursor.fetchall()
# print(s)
sum = 0
count = 0
for i in s:
    c = ','.join([str(c) for c in i])
    print(c)
    sum += int(c[1])+ int(c[5])
    count +=2
s_a = sum / count
print('Среднее арифметическое равно: ', s_a)
cursor.execute("SELECT COUNT(*) from tab_1")
result = cursor.fetchall()
for g in result:
    print('Количество записей в БД: ', g[0])
g_int = g[0]

# Удаление записи из таблицы по id, по значению
if int(s_a) > int(g_int) and int(g_int) >= 4:
    try:
        cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
        newbase.commit()
    except KeyError:
        print('Произошла ошибка KeyError!')
    else:
        print('Ошибок не произошло!')
    finally:
        print('Оператор finally выполнен!')

cursor.execute('''SELECT*FROM tab_1''')
s = cursor.fetchall()
print(s)

