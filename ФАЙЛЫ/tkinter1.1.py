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
    oval = canvas.create_oval((lol, 0), (lol+50, 50), fill='LimeGreen')
    oval = canvas.create_oval((lol+50, 50), (lol + 100, 100), fill='LimeGreen')
    oval = canvas.create_oval((lol, 100), (lol+50, 150), fill='LimeGreen')

for lol2 in range(-50,400,100):
    l = canvas.create_line((lol2, 0), (lol2+50, 50),(lol2, 50), (lol2+50, 0), fill='red')
    l = canvas.create_line((lol2+50, 50), (lol2 + 100, 100), (lol2+50, 100), (lol2 + 100, 50), fill='red')
    l = canvas.create_line((lol2, 150), (lol2 + 50, 100), (lol2, 100), (lol2 + 50, 150), fill='red')
    l = canvas.create_line((lol2+50, 200), (lol2 + 100, 150), (lol2+50, 150), (lol2 + 100, 200), fill='red')
    l = canvas.create_line((lol2, 250), (lol2 + 50, 200), (lol2, 200), (lol2 + 50, 250), fill='red')
    l = canvas.create_line((lol2+50, 300), (lol2 + 100, 250), (lol2+50, 250), (lol2 + 100, 300), fill='red')
    l = canvas.create_line((lol2, 350), (lol2 + 50, 300), (lol2, 300), (lol2 + 50, 350), fill='red')
    l = canvas.create_line((lol2+50, 400), (lol2 + 100, 350), (lol2 + 50, 350), (lol2 + 100, 400), fill='red')



for lol2 in range(0,400,100):
    oval = canvas.create_oval((lol2+50, 250), (lol2+100,300), fill='DeepSkyBlue')
    oval = canvas.create_oval((lol2, 300), (lol2 + 50, 350), fill='DeepSkyBlue')
    oval = canvas.create_oval((lol2+50, 350), (lol2+100, 400), fill='DeepSkyBlue')

canvas.pack()
win.bind("<KeyPress>", move_by_keys)

win.mainloop()
