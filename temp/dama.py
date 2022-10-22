# from tkinter import *
# from tkinter import ttk

# def font_size_up(label : Label):
#     label.cget("font")
#     label.config(font=('',20,''))

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# hello_label = ttk.Label(frm, text="Hello World!", font=('',10,''))
# hello_label.grid(column=0, row=0)
# ttk.Button(frm, text="size up!", command=(lambda : font_size_up(hello_label))).grid(column=1, row=0)
# # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# root.mainloop()


from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="hello", command=lambda: print(
    "안녕하세요")).grid(column=1, row=0)
root.mainloop()
