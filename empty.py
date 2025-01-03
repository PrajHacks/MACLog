import sqlite3

conn = sqlite3.connect('attendance.db')
c = conn.cursor()

c.execute('DELETE FROM attend;',)

print('We have deleted', c.rowcount, 'records from the table.')
		
conn.commit()
conn.close()