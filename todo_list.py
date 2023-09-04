import tkinter
import tkinter.messagebox 
import pickle # This library is used to store the data in a file.
from tkinter import * # from tkinter library we are importing everything.

root = tkinter.Tk()
root.title("To-Do-List App")
root.geometry("650x650+500+100")
root.resizable(True, True)

# Defining the buttons between line number 48 and 58
def add_task():
    task = entry_task.get()
    if task !="":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)  # I added this line because till line number 21 i was able to add the task but wasn't able to clear what is write in the text box.
    else:
        tkinter.messagebox.showwarning(title="ERROR!", message="Task cannot be empty, add a task!") # I added this line because without this line i was able to add empty tasks too which is a blunder.

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="ERROR!", message="Choose a task which is to be deleted") # This line was added because if none of the task is chosen to delete so this message should appear.

def load_task():
    try:
        tasks = pickle.load(open("todotasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="ERROR!", message="File not found") # Added this line because whenever someone adds some tasks and doesnt saves them, and due to n number of reasons if he deletes some of them so he should get and error i.e. file not found.

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("todotasks.dat","wb"))

# Creating GUI for the App
mainframe_tasks = tkinter.Frame(root, bg="black")
mainframe_tasks.pack()

listbox_tasks = tkinter.Listbox(mainframe_tasks, height=30, width=92)
listbox_tasks.pack(side=tkinter.LEFT)

Scrollbar_tasks = tkinter.Scrollbar(mainframe_tasks)
Scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=Scrollbar_tasks.set)
Scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width= 50,)
entry_task.pack()

# Now we will add some buttons to add, delete, load and save the tasks 
button_add_tasks = tkinter.Button(root, text="Click to Add the Tasks", width=50, command=add_task)
button_add_tasks.pack()

button_delete_tasks = tkinter.Button(root, text="Click to Delete the Tasks", width=50, command=delete_task)
button_delete_tasks.pack()

button_load_tasks = tkinter.Button(root, text="Click to Load the Tasks", width=50, command=load_task)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Click to Save the Tasks", width=50, command=save_task)
button_save_tasks.pack()

root.mainloop()