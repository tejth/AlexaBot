import csv
import sqlite3
conn = sqlite3.connect("alexa.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key , name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null,'one note','C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office OneNote 2007.lnk')"
# cursor.execute(query)
# conn.commit();

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key , name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null,'java point','https://www.javatpoint.com/')"
# cursor.execute(query)
# conn.commit();

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# desired_columns_indices = [0, 30]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
# conn.commit()
# conn.close()

# query = "INSERT INTO contacts VALUES (null,'mata ji', '639sda523916602',null)"
# cursor.execute(query)
# conn.commit()