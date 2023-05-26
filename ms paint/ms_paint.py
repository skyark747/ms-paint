from asyncio.windows_events import NULL
from cgitb import text
from distutils.command.install import install
from email.mime import image
from textwrap import fill
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from turtle import width
import PIL
from PIL import ImageGrab,Image,ImageTk

class Paint:
    def __init__(self,width,height):
        #screen 
        self.screen=Tk()
        self.screen.title("Soban's Paint")
        self.screen.geometry(str(width)+'x'+str(height))

        #Selection area
        self.buttonarea=Canvas(self.screen,width=width,height=100,highlightbackground="black",highlightthickness=2)
        self.buttonarea.pack()

        self.shapescanvas=Frame(self.buttonarea,width=195,height=100,bg="lightblue",highlightthickness=1,highlightbackground="black")
        self.shapescanvas.place(x=368,y=2)

        self.shapescanvas_1=Frame(self.buttonarea,width=182,height=64,bg="white",highlightbackground="black",highlightthickness=1)
        self.shapescanvas_1.place(x=374,y=16)

        self.colorcanvas=Frame(self.buttonarea,width=400,height=100,bg="mistyrose",highlightthickness=1,highlightbackground="black")
        self.colorcanvas.place(x=765,y=2)

        self.toolsframe=Frame(self.buttonarea,width=130,height=100,highlightthickness=1,highlightbackground="black")
        self.toolsframe.place(x=140,y=2)
    
        #labels
        self.label=Label(self.buttonarea,text="Colors",width=5,bg="mistyrose")
        self.label.place(x=920,y=80)

        self.labelshape=Label(self.buttonarea,text="Shapes",width=5,bg="lightblue")
        self.labelshape.place(x=440,y=80)

        self.labeltools=Label(self.buttonarea,text="Tools",width=5)
        self.labeltools.place(x=185,y=80)

        #Canvas making
        self.canvas=Canvas(self.screen,width=width,height=height,bg="white")
        self.canvas.pack()
        self.canvas.create_rectangle(0,0,width,height,outline="black",width=1)

     
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
        self.clearpic=self.clearpic.subsample(x=48,y=50)

        self.clear=Button(self.buttonarea,image=self.clearpic,command=self.clearbutton,relief="flat")
        self.clear.place(x=5,y=72)

        self.straightlinepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\straightline.PNG")
        self.straightlinepic=self.straightlinepic.subsample(x=20,y=20)

        self.straightline=Button(self.buttonarea,image=self.straightlinepic,bg="lightblue",relief="groove",command=self.obj_shapes.islinebuttonpressed)
        self.straightline.place(x=378,y=20)

        self.circlepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\circle.PNG")
        self.circlepic=self.circlepic.subsample(x=120,y=128)

        self.circle=Button(self.buttonarea,image=self.circlepic,bg="lightblue",relief="groove",command=self.obj_shapes.iscirclebuttonpressed)
        self.circle.place(x=412,y=20)

        self.ovalpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\ovalshape.PNG")
        self.ovalpic=self.ovalpic.subsample(x=65,y=40)

        self.circle=Button(self.buttonarea,image=self.ovalpic,bg="lightblue",relief="groove",command=self.obj_shapes.isovalbuttonpressed)
        self.circle.place(x=447,y=20)

        self.rectanglepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\rectangleshape.PNG")
        self.rectanglepic=self.rectanglepic.subsample(x=23,y=25)

        self.rectangleshape=Button(self.buttonarea,image=self.rectanglepic,bg="lightblue",relief="groove",command=self.obj_shapes.isrectanglebuttonpressed)
        self.rectangleshape.place(x=483,y=20)

        self.squarepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\square.PNG")
        self.squarepic=self.squarepic.subsample(x=60,y=64)

        self.squareshape=Button(self.buttonarea,image=self.squarepic,bg="lightblue",relief="groove",command=self.obj_shapes.issquarebuttonpressed)
        self.squareshape.place(x=520,y=20)

        self.trianglepic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\t1.PNG")
        self.trianglepic=self.trianglepic.subsample(x=37,y=35)

        self.triangleshape=Button(self.buttonarea,image=self.trianglepic,bg="lightblue",relief="groove",command=self.obj_shapes.istrianglebuttonpressed)
        self.triangleshape.place(x=378,y=50)

        self.pentagonpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\pentagon.PNG")
        self.pentagonpic=self.pentagonpic.subsample(x=45,y=50)

        self.pentagonshape=Button(self.buttonarea,image=self.pentagonpic,bg="lightblue",relief="groove",command=self.obj_shapes.ispentagonbuttonpressed)
        self.pentagonshape.place(x=412,y=50)

        self.hexagonpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\hexagon.PNG")
        self.hexagonpic=self.hexagonpic.subsample(x=40,y=47)

        self.hexagonshape=Button(self.buttonarea,image=self.hexagonpic,bg="lightblue",relief="groove",command=self.obj_shapes.ishexagonbuttonpressed)
        self.hexagonshape.place(x=447,y=50)

        self.starpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\st.PNG")
        self.starpic=self.starpic.subsample(x=42,y=45)

        self.starshape=Button(self.buttonarea,image=self.starpic,bg="lightblue",relief="groove",command=self.obj_shapes.isstarbuttonpressed)
        self.starshape.place(x=483,y=50)

        self.rtripic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\t2.PNG")
        self.rtripic=self.rtripic.subsample(x=19,y=25)

        self.rtrishape=Button(self.buttonarea,image=self.rtripic,bg="lightblue",relief="groove",command=self.obj_shapes.isrighttrianglebuttonpressed)
        self.rtrishape.place(x=520,y=50)

        self.pict=PhotoImage(file=r"D:\\ms paint\ms paint\pics\color.PNG")
        self.pict=self.pict.subsample(50,30)
        self.colorbutton=Button(self.buttonarea,image=self.pict,bg="white",relief="groove",command=self.obj_tools.changecolorbrush)
        self.colorbutton.place(x=1040,y=20)

        self.color=Button(self.buttonarea,text="color 2",image=self.pict,bg="white",relief="groove",command=self.obj_tools.changecoloreraser)
        self.color.place(x=1110,y=20)

        self.picred=PhotoImage(file=r"D:\\ms paint\ms paint\pics\red.PNG")
        self.picred=self.picred.subsample(130,90)
     
        self.cl0=Button(self.buttonarea,image=self.picred,bg="white",command=lambda:[self.obj_tools.brushcolor.set("red"),self.obj_tools.clshow.configure(bg="red")],relief="groove")
        self.cl0.place(x=880,y=20)
        

        self.picdarkred=PhotoImage(file=r"D:\\ms paint\ms paint\pics\darkred.PNG")
        self.picdarkred=self.picdarkred.subsample(9,10)
     
        self.cl=Button(self.buttonarea,image=self.picdarkred,bg="white",command=lambda:[self.obj_tools.brushcolor.set("darkred"),self.obj_tools.clshow.configure(bg="darkred")],relief="groove")
        self.cl.place(x=880,y=50)

        self.picorange=PhotoImage(file=r"D:\\ms paint\ms paint\pics\orange.PNG")
        self.picorange=self.picorange.subsample(15,10)
     
        self.cl1=Button(self.buttonarea,image=self.picorange,bg="white",command=lambda:[self.obj_tools.brushcolor.set("orange"),self.obj_tools.clshow.configure(bg="orange")],relief="groove")
        self.cl1.place(x=910,y=20)

        self.picyellow=PhotoImage(file=r"D:\\ms paint\ms paint\pics\yellow.PNG")
        self.picyellow=self.picyellow.subsample(18,10)
     
        self.cl2=Button(self.buttonarea,image=self.picyellow,bg="white",command=lambda:[self.obj_tools.brushcolor.set("yellow"),self.obj_tools.clshow.configure(bg="yellow")],relief="groove")
        self.cl2.place(x=940,y=20)

        self.picgreen=PhotoImage(file=r"D:\\ms paint\ms paint\pics\green.PNG")
        self.picgreen=self.picgreen.subsample(12,10)
     
        self.cl3=Button(self.buttonarea,image=self.picgreen,bg="white",command=lambda:[self.obj_tools.brushcolor.set("green"),self.obj_tools.clshow.configure(bg="green")],relief="groove")
        self.cl3.place(x=970,y=20)

        self.picpurple=PhotoImage(file=r"D:\\ms paint\ms paint\pics\purple.PNG")
        self.picpurple=self.picpurple.subsample(16,10)

        self.cl4=Button(self.buttonarea,image=self.picpurple,bg="white",command=lambda:[self.obj_tools.brushcolor.set("purple"),self.obj_tools.clshow.configure(bg="purple")],relief="groove")
        self.cl4.place(x=1000,y=20)

        self.picbrown=PhotoImage(file=r"D:\\ms paint\ms paint\pics\brown.PNG")
        self.picbrown=self.picbrown.subsample(15,10)

        self.cl5=Button(self.buttonarea,image=self.picbrown,bg="white",command=lambda:[self.obj_tools.brushcolor.set("brown"),self.obj_tools.clshow.configure(bg="brown")],relief="groove")
        self.cl5.place(x=910,y=50)

        self.picparrot=PhotoImage(file=r"D:\\ms paint\ms paint\pics\parrot.PNG")
        self.picparrot=self.picparrot.subsample(17,10)

        self.cl6=Button(self.buttonarea,image=self.picparrot,bg="white",command=lambda:[self.obj_tools.brushcolor.set("yellowgreen"),self.obj_tools.clshow.configure(bg="yellowgreen")],relief="groove")
        self.cl6.place(x=940,y=50)
        
        self.piclightblue=PhotoImage(file=r"D:\\ms paint\ms paint\pics\pink.PNG")
        self.piclightblue=self.piclightblue.subsample(12,10)

        self.cl7=Button(self.buttonarea,image=self.piclightblue,bg="white",command=lambda:[self.obj_tools.brushcolor.set("pink"),self.obj_tools.clshow.configure(bg="pink")],relief="groove")
        self.cl7.place(x=970,y=50)

        self.picturqoise=PhotoImage(file=r"D:\\ms paint\ms paint\pics\turqoise.PNG")
        self.picturqoise=self.picturqoise.subsample(17,10)

        self.cl8=Button(self.buttonarea,image=self.picturqoise,bg="white",command=lambda:[self.obj_tools.brushcolor.set("turquoise"),self.obj_tools.clshow.configure(bg="turquoise")],relief="groove")
        self.cl8.place(x=1000,y=50)

        self.picblue=PhotoImage(file=r"D:\\ms paint\ms paint\pics\bluegrey.PNG")
        self.picblue=self.picblue.subsample(400,250)

        self.cl9=Button(self.buttonarea,image=self.picblue,bg="white",command=lambda:[self.obj_tools.brushcolor.set("blue"),self.obj_tools.clshow.configure(bg="blue")],relief="groove")
        self.cl9.place(x=850,y=20)

        self.picblush=PhotoImage(file=r"D:\\ms paint\ms paint\pics\blush.PNG")
        self.picblush=self.picblush.subsample(15,10)

        self.cl10=Button(self.buttonarea,image=self.picblush,bg="white",command=lambda:[self.obj_tools.brushcolor.set("mistyrose"),self.obj_tools.clshow.configure(bg="mistyrose")],relief="groove")
        self.cl10.place(x=850,y=50)


        self.pic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\brush.PNG")
        self.pic=self.pic.subsample(15,13)
        self.brushbutton=Button(self.buttonarea,image=self.pic,bg="white",command=self.obj_tools.isbrushbuttonpressed,relief="groove")
        self.brushbutton.place(x=300,y=20)

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

        self.pbucketpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\balty.PNG")
        self.pbucketpic=self.pbucketpic.subsample(x=10,y=10)
        self.pbucket=Button(self.buttonarea,image=self.pbucketpic,relief="flat",command=self.obj_tools.ispaintbucketbuttonpressed)
        self.pbucket.place(x=190,y=15)

        self.textpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\text.PNG")
        self.textpic=self.textpic.subsample(x=40,y=40)
        self.text=Button(self.buttonarea,image=self.textpic,relief="flat",command=self.text)
        self.text.place(x=230,y=15)

        self.selectionpic=PhotoImage(file=r"D:\\ms paint\ms paint\pics\rectangleshape.PNG")
        self.selectionpic=self.selectionpic.subsample(x=20,y=20)

        self.selectarea=Button(self.buttonarea,image=self.selectionpic,relief="groove",command=self.obj_shapes.isselectbuttonpressed)
        self.selectarea.place(x=63,y=15)

        self.movement=Button(self.buttonarea,text="move",relief="groove",command=self.obj_shapes.ismovement)
        self.movement.place(x=60,y=60)

    def text(self):
        self.write_text=StringVar()
        self.enter=Entry(self.buttonarea,width=20,textvariable=self.write_text)
        self.enter.place(x=1170,y=20)
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")        
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<Button-1>",self.textshow)
    def textshow(self,event):      
        self.canvas.create_text(event.x,event.y,text=self.write_text.get())

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
        self.stroke_size=Scale(self.buttonarea,from_=1,to=10,length=150,bg="red",orient="horizontal",relief="groove",label="Size")
        self.stroke_size.place(x=585,y=20)
        
        self.prev_x,self.prev_y=None,None
           
        #brush color button
        self.clshow=Button(self.buttonarea,width=3,height=2,relief="groove",bg="black")
        self.clshow.place(x=770,y=20)

        #eraser color button
        self.clshow_1=Button(self.buttonarea,width=3,height=2,relief="groove",bg="white")
        self.clshow_1.place(x=810,y=20)
             
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
   
    def changecoloreraser(self):
        selectcolor=colorchooser.askcolor()
        self.erasercolor=selectcolor[1]
        self.clshow_1["bg"]=self.erasercolor

    def zoomin(self,event):
        self.canvas.scale("all",event.x,event.y,1.2,1.2)

    def zoomout(self,event):
        self.canvas.scale("all",event.x,event.y,0.9,0.9)


    def iszoombuttonpressed(self):
        self.canvas["cursor"]="sizing"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<Button-1>",self.zoomin)
        self.canvas.bind("<Button-3>",self.zoomout)


    def colorpicker(self,event):   
        self.color=self.canvas.itemcget(self.canvas.find_closest(event.x,event.y),"fill")
        self.brushcolor.set(self.color)
        self.clshow["bg"]=self.color

         
    def iscolorpickerbuttonpressed(self):
        self.canvas["cursor"]="arrow"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")        
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<Button-1>",self.colorpicker)
        self.canvas.bind("<ButtonRelease-1>",self.brushend)
        
    def floodfill(self,x,y,n,oldcolor,pic,image,target_color): 
    
        #c=pic.getpixel((x,y))
        #color = '#%02x%02x%02x' % c
        #if color ==oldcolor:           
        #   pic.putpixel((x,y),(255,0,0))    
        #   photo_image = ImageTk.PhotoImage(pic)
        #   self.canvas.itemconfig(image, image=photo_image)

        #   self.floodfill(x-n,y,n,oldcolor,pic,image)
               
        #   self.floodfill(x+n,y,n,oldcolor,pic,image)
               
        #   self.floodfill(x,y-n,n,oldcolor,pic,image)
              
        #   self.floodfill(x,y+n,n,oldcolor,pic,image)
             

        #else:
        #    return
        points=[x,y]      
        item=self.canvas.find_enclosed(0,0,1300,700)
        item_2=self.canvas.find_closest(x,y)
        prev_color=StringVar()
        prev_color.set("white")
        if item==():
            self.canvas.itemconfig(item,fill=self.clshow["bg"])
        if item==item_2:
            newcolor=self.canvas.itemcget(item,"fill")
            if target_color != newcolor:
                return
            self.canvas.itemconfig(item,fill=self.clshow["bg"])
            prev_color.set(self.clshow["bg"])
            if item!=item_2:
                newcolor=self.canvas.itemcget(item_2,"fill")
                if target_color != newcolor:
                   return
                self.canvas.itemconfig(item_2,fill=self.clshow["bg"])
                if self.canvas.itemcget(item,"fill")=="":
                    self.canvas.itemconfig(item,fill="white")
                else:
                    return
                self.floodfill(x,y-n,n,oldcolor)
                self.floodfill(x,y+n,n,oldcolor)
                self.floodfill(x+n,y,n,oldcolor)
                self.floodfill(x-n,y,n,oldcolor)
            else:
                return

        elif item!=item_2:
            
            newcolor=self.canvas.itemcget(item_2,"fill")
            if target_color != newcolor:
                return
            self.canvas.itemconfig(item_2,fill=self.clshow["bg"])
            if self.canvas.itemcget(item,"fill")=="":
                    self.canvas.itemconfig(item,fill="white")
            else:
                return

            self.floodfill(x,y-n,n,oldcolor,pic,image,target_color)
            self.floodfill(x,y+n,n,oldcolor,pic,image,target_color)
            self.floodfill(x+n,y,n,oldcolor,pic,image,target_color)
            self.floodfill(x-n,y,n,oldcolor,pic,image,target_color)

    def paintbucket(self,event):
        #x=self.canvas.winfo_rootx()+100
        #y=self.canvas.winfo_rooty()+101
        #fileloc="D:\\ms paint\ms paint\pics\canvas.PNG"

        #self.image=ImageGrab.grab(bbox=(x,y,x+1300,y+690))
        #self.image.save(fileloc)

        #self.img=Image.open(fileloc)

        #self.tkimg=ImageTk.PhotoImage(self.img)

        #pic=self.canvas.create_image(0,0,anchor=NW,image=self.tkimg)
        oldcolor=self.canvas.itemcget(self.canvas.find_closest(event.x,event.y),"fill")
        #c=self.img.getpixel((event.x,event.y))
        #if c!=(0,0,0):
        self.floodfill(event.x,event.y,1,"#ffffff",1,1,oldcolor)
                       
    def ispaintbucketbuttonpressed(self):
        self.canvas["cursor"]="spraycan"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")        
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")
       
        self.canvas.bind("<Button-1>",self.paintbucket)
        self.canvas.bind("<ButtonRelease-1>",self.brushend)



class Shapes:
    def __init__(self,canvasarea,selectionarea,objects):
        self.canvas=canvasarea
        self.buttonarea=selectionarea
        self.paintobjs=objects

        self.prev_x,self.prev_y=None,None
        
        self.shapeid=None
        
        self.end_x,self.end_y=0,0
       
        self.obj=None

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
            
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)
    
        x1=self.prev_x
        y1=self.prev_y-radius

        x2=self.prev_x+radius
        y2=self.prev_y

        x3=self.prev_x-radius
        y3=self.prev_y

        x4=x2-radius/2
        y4=self.prev_y+radius
       
        x5=x3+radius/2
        y5=y4

        points=[x5,y5,x3,y3,x1,y1,x2,y2,x4,y4]

        self.shapeid=self.canvas.create_polygon(points,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
       
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
           
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y-radius

        x2=self.prev_x+radius
        y2=self.prev_y

        x3=self.prev_x-radius
        y3=self.prev_y

        x4=x2
        y4=self.prev_y+radius
       
        x5=x3
        y5=y4

        x6=x1
        y6=self.prev_y+2*radius

        points=[x6,y6,x5,y5,x3,y3,x1,y1,x2,y2,x4,y4]

        self.shapeid=self.canvas.create_polygon(points,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
  
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
                        
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return
        radius=abs(self.prev_x-event.x)+abs(self.prev_y-event.y)

        x1=self.prev_x
        y1=self.prev_y-radius

        x2=self.prev_x+radius/2
        y2=self.prev_y

        x3=self.prev_x-radius/2
        y3=y2

        x4=x1+2*radius
        y4=self.prev_y
       
        x5=x1-2*radius
        y5=y4

        x6=x1-0.8*radius
        y6=self.prev_y+radius/1.5

        x7=x1+0.8*radius
        y7=y6

        x8=x3-radius
        y8=self.prev_y+2*radius

        x9=x2+radius
        y9=y8

        x10=self.prev_x
        y10=y3+1.13*radius
       
        points=[x8,y8,x6,y6,x5,y5,x3,y3,x1,y1,x2,y2,x4,y4,x7,y7,x9,y9,x10,y10]
        
        self.shapeid=self.canvas.create_polygon(points,outline=self.paintobjs.brushcolor.get(),width=self.paintobjs.stroke_size.get(),fill="")
   
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
        self.wall=self.shapeid

    def isrighttrianglebuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.righttriangle)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)
        
    def selection_area(self,event):
        if self.shapeid is not None:
            self.canvas.delete(self.shapeid)
        if self.prev_x==None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y
            return

        self.shapeid=self.canvas.create_rectangle(self.prev_x,self.prev_y,event.x,event.y,outline="black",width="1")
        
        self.flag=False
    def startselecting(self,event):
        if self.prev_x == None or self.prev_y==None:
            self.prev_x,self.prev_y=event.x,event.y

        item=[]
        self.selected_item=self.canvas.find_closest(self.prev_x,self.prev_y)
        item=self.canvas.coords(self.selected_item)
        self.obj=self.canvas.find_enclosed(item[0],item[1],item[2],item[3])
 
        if self.flag==False:
            self.canvas.create_rectangle(item[0],item[1],item[2],item[3],width="1",fill=self.paintobjs.clshow_1["bg"],outline=self.paintobjs.clshow_1["bg"])
            self.flag=True
        else:
            return
        
    def endselecting(self,event):
        self.end_x,self.end_y=None,None
        self.prev_x,self.prev_y=None,None
        self.selected_item=None

    def moveselectedarea(self,event):
        if self.selected_item is not None:
            x=event.x-self.prev_x
            y=event.y-self.prev_y

            self.prev_x=self.prev_x+x
            self.prev_y=self.prev_y+y
            
            self.canvas.move(self.selected_item,x,y)
            self.canvas.move(self.obj,x,y)

    def isselectbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.selection_area)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def ismovement(self):
        self.canvas.unbind("<B1-Motion>")     
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")


        self.canvas.bind("<Button-1>", self.startselecting)
        self.canvas.bind("<B1-Motion>", self.moveselectedarea)
        self.canvas.bind("<ButtonRelease-1>", self.endselecting)

    def shapeend(self,event):
        self.prev_x,self.prev_y=None,None
        self.shapeid=None
 

Paint(1300,700).play()
