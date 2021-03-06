from tkinter import *
from math import *
root = Tk()

SIZE = 600

canvas = Canvas(root, width=SIZE, height=SIZE, bg="#f0fff0")
canvas.pack()


def drawhexa(d,x,y,size):
    h = sqrt(size**2 - (size/2)**2)
    if d < 1:
        return
    
    canvas.create_polygon(x,y,
    x + size/2, y - h,
    x + 3/2 * size, y - h,
    x + 2 * size, y,
    x + 3/2 * size, y + h,
    x + size/2, y + h, fill="#070707", outline="#f7f7f7")

    drawhexa(d-1,x,y,size/3)
    drawhexa(d-1,x + size/3,y - 2/3*h, size/3)
    drawhexa(d-1,x + size,y - 2/3*h, size/3)
    drawhexa(d-1,x + 4/3*size,y, size/3)
    drawhexa(d-1,x + size/3,y + 2/3*h, size/3)
    drawhexa(d-1,x + size,y + 2/3*h, size/3)

drawhexa(5,5,300,298)

root.mainloop()