
from tkinter import *
from turtle import title

class Paint:
    def __init__(self,width,height,color):
        #screen 
        self.screen=Tk()
        self.screen.title("Paint")
        self.screen.geometry(str(width)+'x'+str(height))

        #Selection area
        self.buttonarea=Canvas(self.screen,width=width,height=100,highlightbackground="black",highlightthickness=1)
        self.buttonarea.pack()

        #Canvas making
        self.canvas=Canvas(self.screen,width=width,height=height,bg=color)
        self.canvas.pack()

        #Button making
        self.clear=Button(self.buttonarea,bitmap="error",bg="white",command=self.clearbutton)
        self.clear.place(x=5,y=70)

        self.eraser=Button(self.buttonarea,bitmap="error",bg="white",command=self.eraser)
        self.eraser.place(x=100,y=20)

        #canvas bind
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

    def clearbutton(self):
        self.canvas.delete("all")

Paint(1300,700,"white").play()
