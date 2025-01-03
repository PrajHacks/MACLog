import sqlite3


#database connection
conn =  sqlite3.connect("attendance.db")      
c = conn.cursor()


#Create two tables named userdata and Attend
# c.execute('''CREATE TABLE userdata
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               username TEXT NOT NULL,
#               mac_address TEXT NOT NULL)''')
# c.execute('''
#   CREATE TABLE Attend (
#     aid INTEGER PRIMARY KEY,
#     user_id INTEGER,
#     entry_time DATETIME,
#     exit_time DATETIME,
#     today_date DATE,
#     FOREIGN KEY (user_id) REFERENCES userdata(id)
#   )
# ''')


# insert statement for userdata
# c.execute('''
#     INSERT INTO userdata(
#         username,mac_address)
#         VALUES('Amey','8c:8d:28:ac:02:88')
# ''')
# conn.commit()

# c.execute('''
#     DELETE FROM Attend
# ''')
# conn.commit()


def check_mac(mac_address):
    import sqlite3
    import datetime
    match = []    
    for mac in mac_address:
        c.execute('SELECT id FROM userdata WHERE mac_address=?', (mac,))
        result = c.fetchall()
        id_list = [row[0] for row in result]
        if result:
            match.append(id_list[0])
    print(match)
    for id_to_check in match:
        result = None
        c.execute("SELECT user_id FROM Attend WHERE user_id=? AND exit_time IS NULL", (id_to_check,))
        result = c.fetchone()  

        from datetime import date
        entry_time = datetime.datetime.now()
        date = date.today()
        
        if result is None:
            exit_time = None
            
            c.execute("INSERT INTO Attend (user_id, entry_time, exit_time, today_date) VALUES (?, ?, ?, ?)",(id_to_check, entry_time, exit_time, date))            
            conn.commit()
        else:
            c.execute('SELECT id FROM userdata')
            id_list = c.fetchall()
            for id_value in id_list:
                if id_value[0] not in match:
                    exit_time = datetime.datetime.now()
                    c.execute('UPDATE Attend SET exit_time = ? WHERE user_id = ? AND exit_time IS NULL', (exit_time, id_value[0]))
                    conn.commit()   