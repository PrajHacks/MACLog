import tkinter as tk
from tkinter import ttk
import sqlite3 
import subprocess
import PIL  
from PIL import ImageTk
from PIL import Image
from tkinter import *
from datetime import datetime
from tkcalendar import Calendar

root = tk.Tk()
root.title("Attendance System")
root.geometry("1280x720")


tab_control = ttk.Notebook(root)
tab3 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Start System')
tab_control.add(tab1, text='Attendee Data')
tab_control.add(tab2, text='Attendance Database')

def start_stop():
    global process

    if process is None:
        process = subprocess.Popen(['python', 'getmac.py'])
        button1.config(text='Stop')
    else:
        process.terminate()
        process = None
        button1.config(text='Start')

def on_close():
    global process

    if process is not None:
        process.terminate() 
    root.destroy() 


root.protocol("WM_DELETE_WINDOW", on_close) 
button1 = tk.Button(tab3, text='Start the attendance system', command=start_stop, width=30, height= 2)
button1.pack(pady=50)

label = Label(tab3)
label.pack(pady=40)






process = None 

tree = ttk.Treeview(tab1)

def add_data():
    username = username_entry.get()
    mac_address = mac_entry.get()

    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()
    c.execute("INSERT INTO userdata (username, mac_address) VALUES (?, ?)", (username, mac_address))
    conn.commit()
    conn.close()

    username_entry.delete(0, tk.END)
    mac_entry.delete(0, tk.END)

    reload_gui()

def reload_gui():
    tree.delete(*tree.get_children())

    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute("SELECT * FROM userdata")
    data = c.fetchall()
    conn.close()

    for row in data:
        tree.insert('', tk.END, values=row)

def delete_record():
    id = id_entry.get()

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM userdata WHERE id=?", (id,))
    conn.commit()

    conn.close()

    id_entry.delete(0, tk.END)

    status_label.config(text="")

    reload_gui()

username_label = tk.Label(tab1, text="Username:")
username_label.pack()
username_entry = tk.Entry(tab1)
username_entry.pack()

mac_label = tk.Label(tab1, text="MAC Address:")
mac_label.pack()
mac_entry = tk.Entry(tab1)
mac_entry.pack()

add_button = tk.Button(tab1, text="Add", command=add_data)
add_button.pack()

id_label = tk.Label(tab1, text="ID:")
id_entry = tk.Entry(tab1)
delete_button = tk.Button(tab1, text="Delete", command=delete_record)
status_label = tk.Label(tab1, text="")
id_label.pack()
id_entry.pack()
delete_button.pack()
status_label.pack()

tree['columns'] = ('ID', 'Name', 'Mac')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=100)
tree.column('Name', anchor=tk.CENTER, width=150)
tree.column('Mac', anchor=tk.CENTER, width=100)

tree.heading('#0', text='', anchor=tk.CENTER)
tree.heading('ID', text='ID', anchor=tk.CENTER)
tree.heading('Name', text='Name', anchor=tk.CENTER)
tree.heading('Mac', text= 'Mac', anchor=tk.CENTER)

conn = sqlite3.connect('attendance.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM userdata'):

    tree.insert('', tk.END, text='', values=row)

tree.pack(expand=tk.YES, fill=tk.BOTH)

tab_control.pack(expand=1, fill='both')

def print_date():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    selected_date = datetime.strptime(cal.get_date(), '%m/%d/%y')
    formatted_date = selected_date.strftime('%Y-%m-%d')
    print(formatted_date)
    user_id = combo.get()
    print(user_id)
    if user_id != "":
        from logtime import logtimecalc
        a= logtimecalc(formatted_date, user_id)
        result_label.config(text=f"Total Log time : {a}",font=("Arial", 16))
        c.execute("select * from Attend where today_date  = ? AND user_id = ?", (formatted_date, user_id))
        print_date = c.fetchall()
        print(print_date)
    else:
        result_label.config(text="")
        c.execute("select * from Attend where today_date  = ?", (formatted_date,))
        print_date = c.fetchall()
        print(print_date)
    
    for row in treeview.get_children():
        treeview.delete(row)
    
    for row in print_date:
        treeview.insert("", tk.END, values=row)

label = tk.Label(tab2, text="Select a employee by ID")
label.pack()

combo = ttk.Combobox(tab2, state="readonly")
combo.pack()

cal = Calendar(tab2, selectmode='day', year=2023, month=3, day=21)
cal.pack(pady=20)

combo['values'] = [""] 
conn = sqlite3.connect('attendance.db')
c = conn.cursor()
c.execute("SELECT id FROM userdata")
user_ids = [row[0] for row in c.fetchall()]
combo['values'] += tuple(user_ids)
treeview = ttk.Treeview(tab2, show='headings')
treeview['columns'] = ('ID', 'UID', 'Entry_time', 'Exit_time','today_date')
treeview.heading('ID', text='ID')
treeview.heading('UID', text='UID')
treeview.heading('Entry_time', text='Entry time')
treeview.heading('Exit_time', text='Exit time')
treeview.heading('today_date', text='Entry Date')

font = ("Arial", 16)

treeview.column('ID', width=50,)
treeview.column('UID', width=100)
treeview.column('Entry_time', width=150)
treeview.column('Exit_time', width=150)
treeview.column('today_date', width=100)
button = ttk.Button(tab2, text="Get Data", command=print_date)
button.pack(pady=20)
treeview.pack()
result_label = tk.Label(tab2, text="",width=30,height=2)
result_label.pack()


root.mainloop()