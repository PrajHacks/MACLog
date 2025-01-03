from datetime import datetime
import sqlite3
import time 

def logtimecalc(formatted_date, user_id):
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()
    c.execute("SELECT entry_time, exit_time FROM Attend WHERE user_id = ? AND today_date =?", (user_id, formatted_date))
    
    totallog = 0
    for row in c.fetchall():
        ent_date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
        ext_date = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
        log_time = (ext_date - ent_date).total_seconds()
        totallog += log_time 
    print(totallog)
    hours, remainder = divmod(totallog, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
    return time_str
