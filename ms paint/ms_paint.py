
from asyncio.windows_events import NULL
from cgitb import text
from tkinter import *
from tkinter import colorchooser

class Paint:
    def __init__(self,width,height,color):
        #screen 
        self.screen=Tk()
        self.screen.title("Soban's Paint")
        self.screen.geometry(str(width)+'x'+str(height))

        #Selection area
        self.buttonarea=Canvas(self.screen,width=width,height=100,highlightbackground="black",highlightthickness=2)
        self.buttonarea.pack()

        self.shapescanvas=Frame(self.buttonarea,width=200,height=99,bg="lightblue")
        self.shapescanvas.place(x=370,y=2)

        #Canvas making
        self.canvas=Canvas(self.screen,width=width,height=height,bg=color)
        self.canvas.pack()
    
        #Tools class Composed
        self.obj_tools=Tools(self.canvas,self.buttonarea)

        #Shapes class Composed
        self.obj_shapes=Shapes(self.canvas,self.buttonarea,self.obj_tools)

        #Button making
        self.clear=Button(self.buttonarea,bitmap="error",bg="white",command=self.clearbutton)
        self.clear.place(x=5,y=70)

        self.straightlinepic=PhotoImage(file=r"D:\\straightline.PNG")
        self.straightlinepic=self.straightlinepic.subsample(x=20,y=20)

        self.straightline=Button(self.buttonarea,image=self.straightlinepic,bg="lightblue",relief="groove",command=self.obj_shapes.islinebuttonpressed)
        self.straightline.place(x=372,y=6)

        self.pict=PhotoImage(file=r"D:\\color.PNG")
        self.pict=self.pict.subsample(50,30)
        self.colorbutton=Button(self.buttonarea,image=self.pict,bg="white",command=self.obj_tools.changecolorbrush)
        self.colorbutton.place(x=1050,y=20)

        self.color=Button(self.buttonarea,text="color 2",image=self.pict,bg="white",command=self.obj_tools.changecoloreraser)
        self.color.place(x=1150,y=20)

        self.picred=PhotoImage(file=r"D:\\red.PNG")
        self.picred=self.picred.subsample(130,90)
     
        self.cl0=Button(self.buttonarea,image=self.picred,bg="white",command=lambda:self.obj_tools.brushcolor.set("red"))
        self.cl0.place(x=840,y=20)

        self.picdarkred=PhotoImage(file=r"D:\\darkred.PNG")
        self.picdarkred=self.picdarkred.subsample(9,10)
     
        self.cl=Button(self.buttonarea,image=self.picdarkred,bg="white",command=lambda:self.obj_tools.brushcolor.set("darkred"))
        self.cl.place(x=840,y=50)

        self.picorange=PhotoImage(file=r"D:\\orange.PNG")
        self.picorange=self.picorange.subsample(15,10)
     
        self.cl1=Button(self.buttonarea,image=self.picorange,bg="white",command=lambda:self.obj_tools.brushcolor.set("orange"))
        self.cl1.place(x=870,y=20)

        self.picyellow=PhotoImage(file=r"D:\\yellow.PNG")
        self.picyellow=self.picyellow.subsample(18,10)
     
        self.cl2=Button(self.buttonarea,image=self.picyellow,bg="white",command=lambda:self.obj_tools.brushcolor.set("yellow"))
        self.cl2.place(x=900,y=20)

        self.picgreen=PhotoImage(file=r"D:\\green.PNG")
        self.picgreen=self.picgreen.subsample(13,10)
     
        self.cl3=Button(self.buttonarea,image=self.picgreen,bg="white",command=lambda:self.obj_tools.brushcolor.set("green"))
        self.cl3.place(x=930,y=20)

        self.picpurple=PhotoImage(file=r"D:\\purple.PNG")
        self.picpurple=self.picpurple.subsample(16,10)

        self.cl4=Button(self.buttonarea,image=self.picpurple,bg="white",command=lambda:self.obj_tools.brushcolor.set("purple"))
        self.cl4.place(x=960,y=20)

        self.picbrown=PhotoImage(file=r"D:\\brown.PNG")
        self.picbrown=self.picbrown.subsample(15,10)

        self.cl5=Button(self.buttonarea,image=self.picbrown,bg="white",command=lambda:self.obj_tools.brushcolor.set("brown"))
        self.cl5.place(x=870,y=50)

        self.picparrot=PhotoImage(file=r"D:\\parrot.PNG")
        self.picparrot=self.picparrot.subsample(17,10)

        self.cl6=Button(self.buttonarea,image=self.picparrot,bg="white",command=lambda:self.obj_tools.brushcolor.set("yellowgreen"))
        self.cl6.place(x=900,y=50)
        
        self.piclightblue=PhotoImage(file=r"D:\\pink.PNG")
        self.piclightblue=self.piclightblue.subsample(14,10)

        self.cl7=Button(self.buttonarea,image=self.piclightblue,bg="white",command=lambda:self.obj_tools.brushcolor.set("pink"))
        self.cl7.place(x=930,y=50)

        self.picturqoise=PhotoImage(file=r"D:\\turqoise.PNG")
        self.picturqoise=self.picturqoise.subsample(17,10)

        self.cl8=Button(self.buttonarea,image=self.picturqoise,bg="white",command=lambda:self.obj_tools.brushcolor.set("turquoise"))
        self.cl8.place(x=960,y=50)


        self.pic=PhotoImage(file=r"D:\\brush.PNG")
        self.pic=self.pic.subsample(15,15)
        self.brushbutton=Button(self.buttonarea,image=self.pic,bg="white",command=self.obj_tools.isbrushbuttonpressed)
        self.brushbutton.place(x=300,y=6)

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
        self.brushcolor=StringVar()
        self.brushcolor.set("black")
        self.prevcolor=StringVar()
        self.prevcolor.set("black")
        self.erasercolor="white"

        #Stroke size
        self.stroke_size=IntVar()
        self.options=[1,3,5,7,9]    
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
        self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=self.stroke_size.get(),capstyle=ROUND,fill=self.brushcolor.get())
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
        self.brushcolor.set(selectcolor[1])
        if selectcolor!=None:
            self.remembercolor()
        if selectcolor==None:
            self.brushcolor.set(self.prevcolor.get())
   
    def remembercolor(self):
        self.prevcolor.set(self.brushcolor.get())

    def changecoloreraser(self):
        selectcolor=colorchooser.askcolor()
        self.erasercolor=selectcolor[1]
    

class Shapes:
    def __init__(self,canvasarea,selectionarea,objects):
        self.canvas=canvasarea
        self.buttonarea=selectionarea
        self.paintobjs=objects

        self.prev_x,self.prev_y=None,None
        self.last_x,self.last_y=None,None

        self.shapeid=None

    def straightline(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return

        self.shapeid=self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=self.paintobjs.stroke_size.get(),fill=self.paintobjs.brushcolor.get())
             
    def islinebuttonpressed(self):
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.straightline)
        self.canvas.bind("<ButtonRelease-1>",self.straightlineend)

    def straightlineend(self,event):
        self.prev_x,self.prev_y=None,None
        self.shapeid=None



Paint(1300,700,"white").play()
