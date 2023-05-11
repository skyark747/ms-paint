
from tkinter import *
from turtle import color

class Paint:
    def __init__(self,width,height,color):
        self.screen=Tk()
        self.screen.title("Paint")
        self.screen.geometry(str(width)+'x'+str(height))

        self.canvas=Canvas(self.screen,width=width,height=height,bg=color)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>",self.brush)
        
        self.canvas.bind("<ButtonRelease-1>",self.brushend)
            

        self.prev_x,self.prev_y=None,None

    def play(self):
        self.screen.mainloop()
    
  
    def brush(self,event):
        if self.prev_x==None or self.prev_x==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=2,capstyle='round',fill="black")
        self.prev_x,self.prev_y=event.x,event.y
     
    def brushend(self,event):
        self.prev_x,self.prev_y=None,None

    def eraser(self,event):
        if self.prev_x==None or self.prev_x==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=3,fill="white")
        self.prev_x,self.prev_y=event.x,event.y

    def eraserend(self,event):
         self.prev_x,self.prev_y=None,None

Paint(1300,700,"white").play()
