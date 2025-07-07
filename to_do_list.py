# IMPORT ALL THE NECESSARY MODULES

import tkinter as tk 
from tkinter import messagebox as msgbox
import json,os


#initialise a json file for storing the data efficiently 

TASK_FILE="tasks.json"

#load the tasks from the json file

def open_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,"r") as new_file:
            return json.load(new_file)
    else:
        return []

#update the json file and save the tasks 

def update_tasks():
    with open(TASK_FILE, "w") as new_file:
        json.dump(tasks,new_file)


#adding a new task

def add_task():
    task = task_input.get()
    if task.strip()=="":
        msgbox.showwarning("Input Error","Empty Task cannot be Added.")
    else:
        tasks.append({"task":task,"done":False})
        update_tasks()
        task_input.delete(0,tk.END)
        refresh_task()


#marking a task as DONE/UNDONE

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_tasks()
        refresh_task()
    except IndexError:
        msgbox.showwarning("Selection Error", "No task selected.")


#deleting a selected task 

def delete_task():
    try:
        selection=task_listbox.curselection()[0]
        tasks.pop(selection)
        update_tasks()
        refresh_task()
    except IndexError:
        msgbox.showwarning("Selection Error", "No task selected.")


#refresh the display for the task_listbox

def refresh_task():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        display = f"[✓] {task['task']}" if task["done"] else f"[ ] {task['task']}"
        task_listbox.insert(tk.END, display)



#setup the GUI

root = tk.Tk()
root.title("TO-DO-APP LIST")

tasks = open_tasks()

frame = tk.Frame(root)
frame.pack(pady=20)

task_input = tk.Entry(frame,font=("helvetica",15), bg="#ea76c0", fg="black", width=40)
task_input.grid(row=0, column=0, padx=20)

add_button = tk.Button(frame, text="Add Task",font=("helvetica",20), bg="#57b9e3", fg="white", width=30, command=add_task)
add_button.grid(row=0, column=1, padx=20)

task_listbox = tk.Listbox(root,font=("helvetica",15), bg="#d5fa84", fg="black",width=80, height=20)
task_listbox.pack(pady=20)

done_button = tk.Button(root, text="Mark Done/Undone",font=("helvetica",20), bg="#58a351", fg="white",width=40, command=mark_done)
done_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task",font=("helvetica",20), bg="#f44040", fg="white", width=40, command=delete_task)
delete_button.pack(pady=10)

refresh_task()

root.mainloop()
