
from tkinter import *
from tkinter import colorchooser

class Paint:
    def __init__(self,width,height,color):
        #screen 
        self.screen=Tk()
        self.screen.title("Soban's Paint")
        self.screen.geometry(str(width)+'x'+str(height))

        #Selection area
        self.buttonarea=Canvas(self.screen,width=width,height=100,highlightbackground="black",highlightthickness=1)
        self.buttonarea.pack()

        #Canvas making
        self.canvas=Canvas(self.screen,width=width,height=height,bg=color)
        self.canvas.pack()
    
        #Tools class Composed
        self.obj_tools=Tools(self.canvas,self.buttonarea)

        #Button making
        self.clear=Button(self.buttonarea,bitmap="error",bg="white",command=self.clearbutton)
        self.clear.place(x=5,y=70)

        self.pict=PhotoImage(file=r"D:\\color.PNG")
        self.pict=self.pict.subsample(15,10)
        self.colorbutton=Button(self.buttonarea,image=self.pict,bg="white",command=self.obj_tools.changecolorbrush)
        self.colorbutton.place(x=1000,y=20)

        #self.color=Button(self.buttonarea,image=self.pict,text="color 2",bg="white",command=self.obj_tools.changecoloreraser)
        #self.color.place(x=1100,y=20)


        self.pic=PhotoImage(file=r"D:\\brush.PNG")
        self.pic=self.pic.subsample(20,20)
        self.brushbutton=Button(self.buttonarea,image=self.pic,bg="white",command=self.obj_tools.isbrushbuttonpressed)
        self.brushbutton.place(x=300,y=20)

        self.picture=PhotoImage(file=r"D:\\th.PNG")
        self.picture=self.picture.subsample(20,20)
        self.eraserpress=Button(self.buttonarea,image=self.picture,bg="white",command=self.obj_tools.iseraserbuttonpressed)
        self.eraserpress.place(x=150,y=20)

    def play(self):
        self.screen.mainloop()
                
    def clearbutton(self):
        self.canvas.delete("all")
  
        
class Tools:
    def __init__(self,Area,Selection):

        self.canvas=Area
        self.buttonarea=Selection
        self.brushcolor="black"
        self.erasercolor="white"

        #Stroke size
        self.stroke_size=IntVar()
        self.options=[1,3,5,7]    
        self.size_list=OptionMenu(self.buttonarea,self.stroke_size,*self.options)
        self.size_list.place(x=600,y=20)

        self.prev_x,self.prev_y=None,None

    def isbrushbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")

        #canvas bind
        self.canvas.bind("<B1-Motion>",self.brush)     
        self.canvas.bind("<ButtonRelease-1>",self.brushend)

    def brush(self,event):          
        if self.prev_x==None or self.prev_x==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=self.stroke_size.get(),capstyle=ROUND,fill=self.brushcolor)
        self.prev_x,self.prev_y=event.x,event.y
    
    def brushend(self,event):
        self.prev_x,self.prev_y=None,None

    def eraser(self,event):
        if self.prev_x==None or self.prev_x==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=self.stroke_size.get(),fill=self.erasercolor)
        self.prev_x,self.prev_y=event.x,event.y

    def eraserend(self,event):
         self.prev_x,self.prev_y=None,None

    def iseraserbuttonpressed(self):
        self.canvas["cursor"]=DOTBOX
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.eraser)
        self.canvas.bind("<ButtonRelease-1>",self.eraserend)

    def changecolorbrush(self):
        selectcolor=colorchooser.askcolor()
        self.brushcolor=selectcolor[1]
   
    def changecoloreraser(self):
        selectcolor=colorchooser.askcolor()
        self.erasercolor=selectcolor[1]


Paint(1300,700,"white").play()
