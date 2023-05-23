from asyncio.windows_events import NULL
from cgitb import text
from email.mime import image
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from turtle import width
import PIL
from PIL import ImageGrab,Image,ImageTk
from tkcolorpicker import askcolor

class Paint:
    def __init__(self,width,height,color):
        #screen 
        self.screen=Tk()
        self.screen.title("Soban's Paint")
        self.screen.geometry(str(width)+'x'+str(height))

        #Selection area
        self.buttonarea=Canvas(self.screen,width=width,height=100,highlightbackground="black",highlightthickness=2)
        self.buttonarea.pack()

        self.shapescanvas=Frame(self.buttonarea,width=182,height=100,bg="lightblue",highlightthickness=1,highlightbackground="black")
        self.shapescanvas.place(x=374,y=2)

        self.colorcanvas=Frame(self.buttonarea,width=365,height=100,bg="mistyrose",highlightthickness=1,highlightbackground="black")
        self.colorcanvas.place(x=765,y=2)

        #labels
        self.label=Label(self.buttonarea,text="Colors",width=5,bg="mistyrose")
        self.label.place(x=910,y=78)

        self.labelshape=Label(self.buttonarea,text="Shapes",width=5,bg="lightblue")
        self.labelshape.place(x=440,y=78)


        #Canvas making
        self.canvas=Canvas(self.screen,width=width,height=height,bg=color)
        self.canvas.pack()
     
        #Tools class Composed
        self.obj_tools=Tools(self.canvas,self.buttonarea)

        #Shapes class Composed
        self.obj_shapes=Shapes(self.canvas,self.buttonarea,self.obj_tools)

        #Scrollbar
        self.scrolly=Scrollbar(self.canvas,bg="black",relief="groove",orient="vertical",command=self.canvas.yview,cursor="arrow")
        self.scrolly.place(x=1281,y=0,height=576)

        self.scrollx=Scrollbar(self.canvas,bg="black",relief="groove",orient="horizontal",command=self.canvas.xview,cursor="arrow")
        self.scrollx.place(x=0,y=576,width=1283)

        #Button making
        self.clearpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\bin.PNG")
        self.clearpic=self.clearpic.subsample(x=50,y=50)

       
        self.clear=Button(self.buttonarea,image=self.clearpic,command=self.clearbutton,relief="flat")
        self.clear.place(x=5,y=72)

        self.straightlinepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\straightline.PNG")
        self.straightlinepic=self.straightlinepic.subsample(x=20,y=20)

        self.straightline=Button(self.buttonarea,image=self.straightlinepic,bg="lightblue",relief="groove",command=self.obj_shapes.islinebuttonpressed)
        self.straightline.place(x=378,y=6)

        self.circlepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\circle.PNG")
        self.circlepic=self.circlepic.subsample(x=120,y=128)

        self.circle=Button(self.buttonarea,image=self.circlepic,bg="lightblue",relief="groove",command=self.obj_shapes.iscirclebuttonpressed)
        self.circle.place(x=412,y=6)

        self.ovalpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\ovalshape.PNG")
        self.ovalpic=self.ovalpic.subsample(x=65,y=40)

        self.circle=Button(self.buttonarea,image=self.ovalpic,bg="lightblue",relief="groove",command=self.obj_shapes.isovalbuttonpressed)
        self.circle.place(x=447,y=6)

        self.rectanglepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\rectangleshape.PNG")
        self.rectanglepic=self.rectanglepic.subsample(x=23,y=25)

        self.rectangleshape=Button(self.buttonarea,image=self.rectanglepic,bg="lightblue",relief="groove",command=self.obj_shapes.isrectanglebuttonpressed)
        self.rectangleshape.place(x=483,y=6)

        self.squarepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\square.PNG")
        self.squarepic=self.squarepic.subsample(x=60,y=64)

        self.squareshape=Button(self.buttonarea,image=self.squarepic,bg="lightblue",relief="groove",command=self.obj_shapes.issquarebuttonpressed)
        self.squareshape.place(x=520,y=6)

        self.trianglepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\t1.PNG")
        self.trianglepic=self.trianglepic.subsample(x=37,y=35)

        self.triangleshape=Button(self.buttonarea,image=self.trianglepic,bg="lightblue",relief="groove",command=self.obj_shapes.istrianglebuttonpressed)
        self.triangleshape.place(x=378,y=40)

        self.pentagonpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\pentagon.PNG")
        self.pentagonpic=self.pentagonpic.subsample(x=45,y=50)

        self.pentagonshape=Button(self.buttonarea,image=self.pentagonpic,bg="lightblue",relief="groove",command=self.obj_shapes.ispentagonbuttonpressed)
        self.pentagonshape.place(x=412,y=40)

        self.hexagonpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\hexagon.PNG")
        self.hexagonpic=self.hexagonpic.subsample(x=40,y=47)

        self.hexagonshape=Button(self.buttonarea,image=self.hexagonpic,bg="lightblue",relief="groove",command=self.obj_shapes.ishexagonbuttonpressed)
        self.hexagonshape.place(x=447,y=40)

        self.starpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\st.PNG")
        self.starpic=self.starpic.subsample(x=42,y=44)

        self.starshape=Button(self.buttonarea,image=self.starpic,bg="lightblue",relief="groove",command=self.obj_shapes.isstarbuttonpressed)
        self.starshape.place(x=483,y=40)

        self.rtripic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\right.PNG")
        self.rtripic=self.rtripic.subsample(x=80,y=73)

        self.rtrishape=Button(self.buttonarea,image=self.rtripic,bg="lightblue",relief="groove",command=self.obj_shapes.isrighttrianglebuttonpressed)
        self.rtrishape.place(x=520,y=40)

        self.pict=PhotoImage(file=r"D:\\ms paint\ms paint\pics\color.PNG")
        self.pict=self.pict.subsample(50,30)
        self.colorbutton=Button(self.buttonarea,image=self.pict,bg="white",relief="groove",command=self.obj_tools.changecolorbrush)
        self.colorbutton.place(x=1000,y=20)

        self.color=Button(self.buttonarea,text="color 2",image=self.pict,bg="white",relief="groove",command=self.obj_tools.changecoloreraser)
        self.color.place(x=1080,y=20)

        self.picred=PhotoImage(file=r"D:\\ms paint\ms paint\pics\red.PNG")
        self.picred=self.picred.subsample(130,90)
     
        self.cl0=Button(self.buttonarea,image=self.picred,bg="white",command=lambda:self.obj_tools.brushcolor.set("red"),relief="groove")
        self.cl0.place(x=840,y=20)
        

        self.picdarkred=PhotoImage(file=r"D:\\ms paint\ms paint\pics\darkred.PNG")
        self.picdarkred=self.picdarkred.subsample(9,10)
     
        self.cl=Button(self.buttonarea,image=self.picdarkred,bg="white",command=lambda:self.obj_tools.brushcolor.set("darkred"),relief="groove")
        self.cl.place(x=840,y=50)

        self.picorange=PhotoImage(file=r"D:\\ms paint\ms paint\pics\orange.PNG")
        self.picorange=self.picorange.subsample(15,10)
     
        self.cl1=Button(self.buttonarea,image=self.picorange,bg="white",command=lambda:self.obj_tools.brushcolor.set("orange"),relief="groove")
        self.cl1.place(x=870,y=20)

        self.picyellow=PhotoImage(file=r"D:\\ms paint\ms paint\pics\yellow.PNG")
        self.picyellow=self.picyellow.subsample(18,10)
     
        self.cl2=Button(self.buttonarea,image=self.picyellow,bg="white",command=lambda:self.obj_tools.brushcolor.set("yellow"),relief="groove")
        self.cl2.place(x=900,y=20)

        self.picgreen=PhotoImage(file=r"D:\\ms paint\ms paint\pics\green.PNG")
        self.picgreen=self.picgreen.subsample(13,10)
     
        self.cl3=Button(self.buttonarea,image=self.picgreen,bg="white",command=lambda:self.obj_tools.brushcolor.set("green"),relief="groove")
        self.cl3.place(x=930,y=20)

        self.picpurple=PhotoImage(file=r"D:\\ms paint\ms paint\pics\purple.PNG")
        self.picpurple=self.picpurple.subsample(16,10)

        self.cl4=Button(self.buttonarea,image=self.picpurple,bg="white",command=lambda:self.obj_tools.brushcolor.set("purple"),relief="groove")
        self.cl4.place(x=960,y=20)

        self.picbrown=PhotoImage(file=r"D:\\ms paint\ms paint\pics\brown.PNG")
        self.picbrown=self.picbrown.subsample(15,10)

        self.cl5=Button(self.buttonarea,image=self.picbrown,bg="white",command=lambda:self.obj_tools.brushcolor.set("brown"),relief="groove")
        self.cl5.place(x=870,y=50)

        self.picparrot=PhotoImage(file=r"D:\\ms paint\ms paint\pics\parrot.PNG")
        self.picparrot=self.picparrot.subsample(17,10)

        self.cl6=Button(self.buttonarea,image=self.picparrot,bg="white",command=lambda:self.obj_tools.brushcolor.set("yellowgreen"),relief="groove")
        self.cl6.place(x=900,y=50)
        
        self.piclightblue=PhotoImage(file=r"D:\\ms paint\ms paint\pics\pink.PNG")
        self.piclightblue=self.piclightblue.subsample(14,10)

        self.cl7=Button(self.buttonarea,image=self.piclightblue,bg="white",command=lambda:self.obj_tools.brushcolor.set("pink"),relief="groove")
        self.cl7.place(x=930,y=50)

        self.picturqoise=PhotoImage(file=r"D:\\ms paint\ms paint\pics\turqoise.PNG")
        self.picturqoise=self.picturqoise.subsample(17,10)

        self.cl8=Button(self.buttonarea,image=self.picturqoise,bg="white",command=lambda:self.obj_tools.brushcolor.set("turquoise"),relief="groove")
        self.cl8.place(x=960,y=50)

        self.picblue=PhotoImage(file=r"D:\\ms paint\ms paint\pics\bluegrey.PNG")
        self.picblue=self.picblue.subsample(400,250)

        self.cl9=Button(self.buttonarea,image=self.picblue,bg="white",command=lambda:self.obj_tools.brushcolor.set("blue"),relief="groove")
        self.cl9.place(x=810,y=20)

        self.picblush=PhotoImage(file=r"D:\\ms paint\ms paint\pics\blush.PNG")
        self.picblush=self.picblush.subsample(15,10)

        self.cl10=Button(self.buttonarea,image=self.picblush,bg="white",command=lambda:self.obj_tools.brushcolor.set("mistyrose"),relief="groove")
        self.cl10.place(x=810,y=50)


        self.pic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\brush.PNG")
        self.pic=self.pic.subsample(15,15)
        self.brushbutton=Button(self.buttonarea,image=self.pic,bg="white",command=self.obj_tools.isbrushbuttonpressed)
        self.brushbutton.place(x=300,y=6)

        self.picture=PhotoImage(file=r"D:\\ms paint\ms paint\pics\eraser1.PNG")
        self.picture=self.picture.subsample(7,7)
        self.eraserpress=Button(self.buttonarea,image=self.picture,relief="flat",command=self.obj_tools.iseraserbuttonpressed)
        self.eraserpress.place(x=150,y=53)

        self.savepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\save.PNG")
        self.savepic=self.savepic.subsample(x=70,y=70)
        self.save=Button(self.buttonarea,image=self.savepic,relief="flat",command=self.save)
        self.save.place(x=3,y=2)

        self.loadpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\upload.PNG")
        self.loadpic=self.loadpic.subsample(x=25,y=25)
       
        self.load=Button(self.buttonarea,image=self.loadpic,relief="flat",command=self.loadimage)
        self.load.place(x=3,y=35)


        self.pencilpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\pencil1.PNG")
        self.pencilpic=self.pencilpic.subsample(x=84,y=84)
        self.pencil=Button(self.buttonarea,image=self.pencilpic,relief="flat",command=self.obj_tools.isbrushbuttonpressed)
        self.pencil.place(x=150,y=15)

        self.zoompic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\zoommag.PNG")
        self.zoompic=self.zoompic.subsample(50,50)

        self.zoombutton=Button(self.buttonarea,image=self.zoompic,command=self.obj_tools.iszoombuttonpressed,relief="flat")
        self.zoombutton.place(x=230,y=53)

        self.colorpickpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\colorpicker.PNG")
        self.colorpickpic=self.colorpickpic.subsample(8,8)

        self.colorpickbutton=Button(self.buttonarea,image=self.colorpickpic,command=self.obj_tools.iscolorpickerbuttonpressed,relief="flat")
        self.colorpickbutton.place(x=190,y=53)


    def save(self):
        self.fileloc=filedialog.asksaveasfilename(defaultextension="PNG",title="select file type",filetypes = (('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),('PNG', '*.png'),('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
        x=self.canvas.winfo_rootx()+100
        y=self.canvas.winfo_rooty()+101

        self.image=ImageGrab.grab(bbox=(x,y,x+1300,y+690))
        self.image.save(self.fileloc)

    def loadimage(self):
        global pic
        self.filename=filedialog.askopenfilename(title="select image",filetypes = (('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),('PNG', '*.png'),('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))
        pic=Image.open(self.filename)
       
        self.tkimg=ImageTk.PhotoImage(pic)
        self.canvas.create_image(0,0,anchor=NW,image=self.tkimg)

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
        self.stroke_size=Scale(self.buttonarea,from_=1,to=9,length=150,bg="red",orient="horizontal",relief="groove",label="Size")
        self.stroke_size.place(x=580,y=20)
        
        self.prev_x,self.prev_y=None,None

        #color show button
        self.clshow=Button(self.buttonarea,width=3,height=2,relief="groove")
        self.clshow.place(x=770,y=20)
        self.clshow["bg"]="black"
       

    def isbrushbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")


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
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.eraser)
        self.canvas.bind("<ButtonRelease-1>",self.eraserend)

    def changecolorbrush(self):
        selectcolor=colorchooser.askcolor()
        self.brushcolor.set(selectcolor[1])
        self.clshow["bg"]=self.brushcolor.get()
        if selectcolor!=None:
            self.remembercolor()
        if selectcolor==None:
            self.brushcolor.set(self.prevcolor.get())
   
    def remembercolor(self):
        self.prevcolor.set(self.brushcolor.get())

    def changecoloreraser(self):
        selectcolor=colorchooser.askcolor()
        self.erasercolor=selectcolor[1]

    def zoomin(self,event):
        self.canvas.scale("all",event.x,event.y,1.2,1.2)

    def zoomout(self,event):
        self.canvas.scale("all",event.x,event.y,0.9,0.9)


    def iszoombuttonpressed(self):
        self.canvas["cursor"]="sizing"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<Button-1>",self.zoomin)
        self.canvas.bind("<Button-3>",self.zoomout)


    def colorpicker(self,event):
        if self.prev_x == None or self.prev_y ==None:
             self.prev_x,self.prev_y=event.x,event.y
             return
         
        self.colorpick=askcolor(parent=self.canvas)
        if self.colorpick[1]:
            self.clshow.config(text="Selected color: " + str(self.colorpick[1]))            
            self.clshow.config(bg=self.colorpick[1])

    def iscolorpickerbuttonpressed(self):
        self.canvas["cursor"]="arrow"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")        
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<Button-1>",self.colorpicker)
        


     

class Shapes:
    def __init__(self,canvasarea,selectionarea,objects):
        self.canvas=canvasarea
        self.buttonarea=selectionarea
        self.paintobjs=objects

        self.prev_x,self.prev_y=None,None
        
        self.shapeid=None
        self.lastid=None
        self.previd=None
        self.newid=None
        self.id1=None
        self.id2=None
        self.id3=None
        self.id4=None

    def straightline(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return

        self.shapeid=self.canvas.create_line(self.prev_x,self.prev_y,event.x,event.y,width=self.paintobjs.stroke_size.get(),fill=self.paintobjs.brushcolor.get())
        
    def circle(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return

        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x-radius/2
        y1=self.prev_y-radius/2

        x2=self.prev_x+radius/2
        y2=self.prev_y+radius/2

        self.shapeid=self.canvas.create_oval(x1,y1,x2,y2,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get())

    def iscirclebuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")


        self.canvas.bind("<B1-Motion>",self.circle)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def islinebuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.straightline)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def oval(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return

        self.shapeid=self.canvas.create_oval(self.prev_x,self.prev_y,event.x,event.y,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get())

  
    def isovalbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.oval)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)
   
    def rectangle(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return

        self.shapeid=self.canvas.create_rectangle(self.prev_x,self.prev_y,event.x,event.y,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get())

  
    def isrectanglebuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")


        self.canvas.bind("<B1-Motion>",self.rectangle)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)


    def square(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y

        x2=self.prev_x+radius/2
        y2=self.prev_y+radius/2

        self.shapeid=self.canvas.create_rectangle(x1,y1,x2,y2,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get())

    def triangle(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y

        x2=self.prev_x-radius/2
        y2=self.prev_y-radius/2

        x3=self.prev_x+radius/2
        y3=self.prev_y+radius/2

        self.shapeid=self.canvas.create_polygon(x1,y1,x3,y3,x2,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
        
    def issquarebuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.square)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def istrianglebuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.triangle)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def pentagon(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
            self.canvas.delete(self.lastid)
            self.canvas.delete(self.newid)
            self.canvas.delete(self.previd)

        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y

        x2=self.prev_x-radius/2
        y2=self.prev_y-radius/2

        x3=self.prev_x+radius/2
        y3=self.prev_y+radius/2

        x4=x1-radius/4
        y4=y1+radius
       
        x5=x1+radius/4
        y5=y1+radius

        self.shapeid=self.canvas.create_polygon(x1,y1,x3,y3,x1,y1,x2,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
   
        self.newid=self.canvas.create_polygon(x4,y4,x2,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
        
        self.previd=self.canvas.create_polygon(x5,y5,x3,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

        self.lastid=self.canvas.create_polygon(x5,y5,x4,y4,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

       
    def ispentagonbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.pentagon)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def hexagon(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
            self.canvas.delete(self.lastid)
            self.canvas.delete(self.newid)
            self.canvas.delete(self.previd)
            self.canvas.delete(self.storeid)

        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y

        x2=self.prev_x-radius/2
        y2=self.prev_y-radius/2

        x3=self.prev_x+radius/2
        y3=self.prev_y+radius/2

        x4=x1-radius/2
        y4=y1+radius
       
        x5=x1+radius/2
        y5=y1+radius

        y6=y1+1.4*radius

        self.shapeid=self.canvas.create_polygon(x1,y1,x3,y3,x1,y1,x2,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
   
        self.newid=self.canvas.create_polygon(x4,y4,x2,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
        
        self.previd=self.canvas.create_polygon(x5,y5,x3,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

        self.lastid=self.canvas.create_polygon(x5,y5,x1,y6,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
       
        self.storeid=self.canvas.create_polygon(x4,y4,x1,y6,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

    def ishexagonbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.hexagon)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def star(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
            self.canvas.delete(self.lastid)
            self.canvas.delete(self.newid)
            self.canvas.delete(self.previd)
            self.canvas.delete(self.storeid)
            self.canvas.delete(self.id1)
            self.canvas.delete(self.id2)
            self.canvas.delete(self.id3)
                        
            self.canvas.delete(self.id4)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y

        x2=self.prev_x-radius/3
        y2=self.prev_y-radius/2

        x3=self.prev_x+radius/3
        y3=self.prev_y+radius/2

        x4=x1-1.3*radius
        y4=y1+radius
       
        x5=x1+1.3*radius
        y5=y1+radius

        x6=x2-radius/3
        y6=y3+radius/2.3
        
        x7=x3+radius/3
        y7=y1+1.5*radius
        
        y8=y1+1.2*radius
        x8=x2-0.7*radius
        x9=x3+0.7*radius

        self.shapeid=self.canvas.create_polygon(x1,y1,x3,y3,x1,y1,x2,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
   
        self.newid=self.canvas.create_polygon(x2,y3,x4,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
        
        self.previd=self.canvas.create_polygon(x5,y3,x3,y3,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

        self.lastid=self.canvas.create_polygon(x5,y3,x7,y6,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
       
        self.storeid=self.canvas.create_polygon(x4,y3,x6,y6,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
        
        self.id1=self.canvas.create_polygon(x6,y6,x8,y7,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

        self.id2=self.canvas.create_polygon(x8,y7,x1,y8,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

        self.id3=self.canvas.create_polygon(x1,y8,x9,y7,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

        self.id4=self.canvas.create_polygon(x9,y7,x7,y6,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

    def isstarbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.star)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)
    
    def righttriangle(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y

        x2=self.prev_x-radius/2
        y2=self.prev_y-radius/2

        x3=self.prev_x+radius/2
        y3=self.prev_y+radius/2

        self.shapeid=self.canvas.create_polygon(x1,y1,x1,y2,x3,y1,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")

    def isrighttrianglebuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.righttriangle)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)


    def shapeend(self,event):
        self.prev_x,self.prev_y=None,None
        self.shapeid=None
        self.previd,self.newid,self.lastid,self.storeid=None,None,None,None
        self.id1,self.id2,self.id3,self.id4=None,None,None,None


Paint(1300,700,"white").play()
