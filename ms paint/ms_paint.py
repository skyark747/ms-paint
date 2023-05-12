
from tkinter import *
from turtle import title


class Paint:
    def __init__(self,width,height,color):
        #screen 
        self.screen=Tk()
        self.screen.title("Soban's Paint")
        self.screen.geometry(str(width)+'x'+str(height))
        
        #attributes
        self.size=2

        #Selection area
        self.buttonarea=Canvas(self.screen,width=width,height=100,highlightbackground="black",highlightthickness=1)
        self.buttonarea.pack()

        #Canvas making
        self.canvas=Canvas(self.screen,width=width,height=height,bg=color)
        self.canvas.pack()

        #Button making
        self.clear=Button(self.buttonarea,bitmap="error",bg="white",command=self.clearbutton)
        self.clear.place(x=5,y=70)


        self.sizebutton=Button(self.buttonarea,bitmap="error",bg="white",command=self.issizebuttonpressed)
        self.sizebutton.place(x=600,y=20)

        self.pic=PhotoImage(file=r"D:\\brush.PNG")
        self.pic=self.pic.subsample(20,20)
        self.brushbutton=Button(self.buttonarea,image=self.pic,bg="white",command=self.isbrushbuttonpressed)
        self.brushbutton.place(x=300,y=20)

        self.picture=PhotoImage(file=r"D:\\th.PNG")
        self.picture=self.picture.subsample(20,20)
        self.eraserpress=Button(self.buttonarea,image=self.picture,bg="white",command=self.iseraserbuttonpressed)
        self.eraserpress.place(x=150,y=20)
           
        self.prev_x,self.prev_y=None,None

    def play(self):
        self.screen.mainloop()
     
      
    def issizebuttonpressed(self):
        self.new=Frame(self.screen,width=150,height=70,bg="pink",highlightbackground="black",highlightthickness=2)
        self.new.place(x=550,y=101)

        self.sizebutton=Button(self.screen,bitmap="error",width=100,height=5,bg="red",highlightbackground="black",
                               highlightthickness=1,command=self.changesize)
        self.sizebutton.place(x=570,y=118)
      
        self.sizebutton2=Button(self.screen,bitmap="error",width=100,height=5,bg="green",highlightbackground="black",
                               highlightthickness=1,command=self.changesize)
        self.sizebutton2.place(x=570,y=137)
        if self.sizebutton2:
            self.sizebutton.deletecommand()
        self.sizebutton3=Button(self.screen,bitmap="error",width=100,height=5,bg="yellow",highlightbackground="black",
                               highlightthickness=1,command=self.changesize)
        self.sizebutton3.place(x=570,y=155)

        
    def changesize(self):
        if self.sizebutton:
            self.size=4
        elif self.sizebutton2:
            self.size=6
        elif self.sizebutton3:
            self.size=8
        else:
            self.size=2

    def isbrushbuttonpressed(self):
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")

        #canvas bind
        self.canvas.bind("<B1-Motion>",self.brush)     
        self.canvas.bind("<ButtonRelease-1>",self.brushend)

    def brush(self,event):      
        if self.prev_x==None or self.prev_x==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=self.size,capstyle='round',fill="black")
        self.prev_x,self.prev_y=event.x,event.y
    
    def brushend(self,event):
        self.prev_x,self.prev_y=None,None

    def eraser(self,event):
        if self.prev_x==None or self.prev_x==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=self.size + 1,fill="white")
        self.prev_x,self.prev_y=event.x,event.y

    def eraserend(self,event):
         self.prev_x,self.prev_y=None,None

    def iseraserbuttonpressed(self):
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.eraser)
        self.canvas.bind("<ButtonRelease-1>",self.eraserend)
        

    def clearbutton(self):
        self.canvas.delete("all")
        self.new.destroy()
        self.sizebutton.destroy()
        self.sizebutton2.destroy()
        self.sizebutton3.destroy()


Paint(1300,700,"white").play()
