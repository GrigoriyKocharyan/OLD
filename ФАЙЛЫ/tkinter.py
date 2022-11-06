import tkinter as tk

def move_by_keys(event):
    if event.keysym == 'Up':
        canvas.move(oval, 0, -4)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 4)
    if event.keysym == 'Left':
        canvas.move(oval, -4, 0)
    if event.keysym == 'Right':
        canvas.move(oval, 4, 0)





win = tk.Tk()
canvas = tk.Canvas(win, bg='#fff', width=700, height=700)
l = canvas.create_line((100,100), (600,100), (600,600), (100,600), (100,100), fill='red')

label = tk.Label(win, text='INGINIRIUM')
label.pack()

oval = canvas.create_oval((300,300),(400,400), fill='yellow')
canvas.pack()
win.bind("<KeyPress>", move_by_keys)


win.mainloop()
