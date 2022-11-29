
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('800x800')

var = tk.StringVar()
t1 = tk.Label(window, text='  ', height=6)
t1.pack()

e = tk.Entry(window)
e.pack()

def insert_point():
    var = e.get()

def insert_end():
    var = e.get()


b1 = tk.Button(window, text='Input directory', width=15,
              height=2, command=insert_point)
b1.pack()


t1 = tk.Label(window, text='  ', height=6)
t1.pack()



def print_selection():
    l.config(text='you have selected ' + var.get())


def case_selection0():
    l.config(text='you have selected Case 0')
    c.config()





r1 = tk.Radiobutton(window, text='Current directory',
                    variable=var, value='Case 0',
                    command=case_selection0)
r1.pack()





r2 = tk.Radiobutton(window, text='List files',
                    variable=var, value='Case 1',
                    command=print_selection)
r2.pack()




r3 = tk.Radiobutton(window, text='Change directory',
                    variable=var, value='Case 2',
                    command=print_selection)
r3.pack()





r4 = tk.Radiobutton(window, text='Remove',
                    variable=var, value='Case 3',
                    command=print_selection)
r4.pack()
r5 = tk.Radiobutton(window, text='Create',
                    variable=var, value='Case 4',
                    command=print_selection)
r5.pack()
r6 = tk.Radiobutton(window, text='Copy',
                    variable=var, value='Case 5',
                    command=print_selection)
r6.pack()
r7 = tk.Radiobutton(window, text='Exit',
                    variable=var, value='Case 6',
                    command=print_selection)
r7.pack()
l = tk.Label(window, bg='white', width=20, text='')
l.pack()




window.mainloop()