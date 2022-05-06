from tkinter import Tk, Button, Label, Scrollbar,Listbox, StringVar, Entry, W, E, N, S,END
from tkinter import ttk
from tkinter import messagebox
from oracle import Bookdb

db = Bookdb()

def get_selected_row(event):
    global selected_tuple
    index = list_bx.curselection()[0]
    selected_tuple = list_bx.get(index)
    title_entry.delete(0, 'end')
    title_entry.insert('end', selected_tuple[1])
    author_entry.delete(0, 'end')
    author_entry.insert('end', selected_tuple[2])
    isbn_entry.delete(0, 'end')
    isbn_entry.insert('end', selected_tuple[3])

def view_records():
    list_bx.delete(0, 'end')
    for row in db.view():
        list_bx.insert('end', row)

def add_book():
    insert_message = db.insert(title_text.get(), author_text.get(), isbn_text.get())

    list_bx.delete(0, 'end')
    list_bx.insert('end', (title_text.get(), author_text.get(), isbn_text.get()))
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')       
    messagebox.showinfo(title="Book database", message=insert_message)

def delete_records():
    delete_message = db.delete(selected_tuple[0])
    messagebox.showinfo(title="Book database", message=delete_message)

def clear_screen():
    list_bx.delete(0, 'end')
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')

def update_records():
    update_message = db.update(selected_tuple[0], title_text.get(), author_text.get(), isbn_text.get())
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')
    messagebox.showinfo(title="Book database", message=update_message)

def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        del dd

root = Tk()

root.title("My Books Database Application")
root.configure(background="light blue")
root.geometry("850x500")
root.resizable(width=False,height=False)


title_label = ttk.Label(root, text="Title",background="light blue",font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root,width=24,textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)



author_label = ttk.Label(root, text="Author",background="light blue",font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root,width=24,textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)


isbn_label = ttk.Label(root, text="ISBN",background="light blue",font=("TkDefaultFont", 16))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root,width=24,textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

add_btn = Button(root, text="Add Book", bg="light gray", fg="gray", font="helvetica 10 bold", command=add_book)
add_btn.grid(row=0, column=6, sticky=W)

list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="light gray")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W +E, pady=40, padx=15)
list_bx.bind('<<ListboxSelect>>', get_selected_row)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

modify_btn = Button(root, text="Modify Record", bg="purple", fg="white", font="helvetica 10 bold", command=update_records)
modify_btn.grid(row=15, column=4)

delete_btn = Button(root, text="Delete Record", bg="red", fg="white", font="helvetica 10 bold", command=delete_records)
delete_btn.grid(row=15, column=5)

view_btn = Button(root, text="View all records", bg="black", fg="white", font="helvetica 10 bold", command=view_records)
view_btn.grid(row=15, column=1)

clear_btn = Button(root, text="Clear screen", bg="maroon", fg="white", font="helvetica 10 bold", command=clear_screen)
clear_btn.grid(row=15, column=2)

clear_btn = Button(root, text="Exit application", bg="blue", fg="white", font="helvetica 10 bold", command=root.destroy)
clear_btn.grid(row=15, column=3)

root.mainloop()



