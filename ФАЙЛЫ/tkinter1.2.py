import tkinter as tk


def move_by_keys(event):
    if event.keysym == 'Up':
            canvas.move(oval, 0, -50)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 50)
    if event.keysym == 'Left':
        canvas.move(oval, -50, 0)
    if event.keysym == 'Right':
        canvas.move(oval, 50, 0)


win = tk.Tk()
canvas = tk.Canvas(win, bg='#fff', width=400, height=400)
for i in range(50,400,50):
    l = canvas.create_line((i, 0), (i, 400),fill='black')

for r in range(50,400,50):
    l = canvas.create_line((0, r), (400, r),fill='black')



label = tk.Label(win, text='INGINIRIUM')
label.pack()

for lol in range(0,400,100):
    cube = canvas.create_rectangle((lol, 0), (lol+50, 50), fill='Black')
    cube = canvas.create_rectangle((lol+50, 50), (lol+100, 100), fill='Black')
    cube = canvas.create_rectangle((lol, 100), (lol+50, 150), fill='Black')
    cube = canvas.create_rectangle((lol+50, 150), (lol+100, 200), fill='Black')
    cube = canvas.create_rectangle((lol, 200), (lol+50, 250), fill='Black')
    cube = canvas.create_rectangle((lol+50, 250), (lol+100, 300), fill='Black')
    cube = canvas.create_rectangle((lol, 300), (lol+50, 350), fill='Black')
    cube = canvas.create_rectangle((lol+50, 350), (lol+100, 400), fill='Black')

for lol in range(-100,400,100):
    cube = canvas.create_rectangle((lol+50, 0), (lol+100, 50), fill='BurlyWood')
    cube = canvas.create_rectangle((lol+100, 50), (lol+150, 100), fill='BurlyWood')
    cube = canvas.create_rectangle((lol+50, 100), (lol+100, 150), fill='BurlyWood')
    cube = canvas.create_rectangle((lol+100, 150), (lol+150, 200), fill='BurlyWood')
    cube = canvas.create_rectangle((lol+50, 200), (lol+100, 250), fill='BurlyWood')
    cube = canvas.create_rectangle((lol+100, 250), (lol+150, 300), fill='BurlyWood')
    cube = canvas.create_rectangle((lol+50, 300), (lol+100, 350), fill='BurlyWood')
    cube = canvas.create_rectangle((lol+100, 350), (lol+150, 400), fill='BurlyWood')

for lol in range(0,400,100):
    oval = canvas.create_oval((lol, 0), (lol+50, 50), fill='LimeGreen')
    oval = canvas.create_oval((lol+50, 50), (lol + 100, 100), fill='LimeGreen')
    oval = canvas.create_oval((lol, 100), (lol+50, 150), fill='LimeGreen')


for lol2 in range(0,400,100):
    oval = canvas.create_oval((lol2+50, 250), (lol2+100,300), fill='DeepSkyBlue')
    oval = canvas.create_oval((lol2, 300), (lol2 + 50, 350), fill='DeepSkyBlue')
    oval = canvas.create_oval((lol2+50, 350), (lol2+100, 400), fill='DeepSkyBlue')

canvas.pack()
win.bind("<KeyPress>", move_by_keys)

win.mainloop()
