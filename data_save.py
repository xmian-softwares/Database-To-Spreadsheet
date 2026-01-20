from tkinter import *
from PIL import ImageTk, Image
from sudent_names import *

def main():
   cav = Tk()
   cav.title("Multiway")
   cav.geometry("580x390+0+0")
   cav.configure(bg='#A92029')
   cav.resizable(False, False)

   path = "main.png"
   load = Image.open(path)
   render = ImageTk.PhotoImage(load)
   cav.iconphoto(False, render)

   clay  = StringVar(value="Tulip")
   clay2  = StringVar(value="Tulip")
   def cla():
      stud1(clay.get())
   def cla2():
      stud2()
   def cla3():
      stud3(clay2.get())
   def cla4():
      stud4()
   def cla5():
      stud5()
   def cla6():
      stud6()
   def cla7():
      stud7()
   def cla8():
      cav.destroy()
   def cla9():
      stud8()
   def cla10():
      stud9()

   up = Frame(cav, bg="crimson")
   up.pack()

   down5 = Frame(cav,relief="raised")
   down5.pack( side = BOTTOM )

   down4 = Frame(cav,relief="raised", bg="#A92029")
   down4.pack( side = BOTTOM )

   down3 = Frame(cav,relief="raised")
   down3.pack( side = BOTTOM )


   down2 = Frame(cav, relief="raised", bg="White")
   down2.pack( side = BOTTOM )

   down = Frame(cav, bg="White",width=385, height=460)
   down.pack(side = BOTTOM)

   image = Image.open("main.png")
   resize_image = image.resize((100, 100))

   img = ImageTk.PhotoImage(resize_image)
   panel = Label(up, image = img,width=100, height=100,bg="crimson")

   F = ("Arial", 23, "bold")
   F2 = ("Arial", 8, "bold")
   Label(up,text=" ",fg="Yellow",bg="crimson",font=F).grid(row=1,column=2,sticky=W)
   Label(up,text="Multi-way School of Language",fg="Yellow",bg="crimson",font=F).grid(row=1,column=3,sticky=W)
   Label(up,text="THE WAY TO A BRIGHT FUTURE!!",fg="white",font=F2,bg="crimson").place(x=120, y=70)
   panel.grid(row=1,column=1,sticky=E)

   Label(down,text=" ",bg="White").grid(row=1,column=1,sticky=W)
   Radiobutton(down,text="Tulip",fg="black",variable=clay, value="Tulip",bg="#88EEBB",font=F2).grid(row=2,column=1,sticky=W)
   Radiobutton(down,text="Wit",fg="black",variable=clay, value="Wit",bg="#EE8888",font=F2).grid(row=2,column=2,sticky=W)
   Radiobutton(down,text="Stunning",fg="black",variable=clay, value="Stunning",bg="#88BBFF",font=F2).grid(row=2,column=4,sticky=W)
   Radiobutton(down,text="Impeccable",fg="black",variable=clay, value="Impeccable",bg="#AADDAA",font=F2).grid(row=2,column=5,sticky=W)

   Label(down,text=" ",bg="White",width=2).grid(row=2,column=6,sticky=W)
   Button(down,text="Print Students",fg="White",bg="Dark Green",width=18,height=1,command=cla).grid(row=2,column=7,sticky=W)

   Label(down,text=":",bg="White").grid(row=2,column=8,sticky=W)
   Button(down,text="Print All Students",fg="White",bg="Dark Blue",width=18,height=1,command=cla2).grid(row=2,column=9,sticky=W)

   Label(down,text="",bg="White").grid(row=3,column=1,sticky=W)
   Radiobutton(down,text="Tulip",fg="black",variable=clay2, value="Tulip",bg="#88EEBB",font=F2).grid(row=4,column=1,sticky=W)
   Radiobutton(down,text="Wit",fg="black",variable=clay2, value="Wit",bg="#EE8888",font=F2).grid(row=4,column=2,sticky=W)
   Radiobutton(down,text="Stunning",fg="black",variable=clay2, value="Stunning",bg="#88BBFF",font=F2).grid(row=4,column=4,sticky=W)
   Radiobutton(down,text="Impeccable",fg="black",variable=clay2, value="Impeccable",bg="#AADDAA",font=F2).grid(row=4,column=5,sticky=W)

   Label(down,text=" ",bg="White").grid(row=4,column=6,sticky=W)
   Button(down,text="Print Results",fg="White",bg="Dark Green",width=18,height=1,command=cla3).grid(row=4,column=7,sticky=W)

   Label(down,text=":",bg="White").grid(row=4,column=8,sticky=W)
   Button(down,text="Print All Result",fg="White",bg="Dark Blue",width=18,height=1,command=cla4).grid(row=4,column=9,sticky=W)

   Label(down2,text=" ",width=2, bg="White").grid(row=5,column=8,sticky=W)
   Button(down2,text="Print Daily Report",fg="White",bg="Dark Red",width=38,height=1,command=cla5).grid(row=8,column=7,sticky=W)

   Label(down2,text=" ", bg="White").grid(row=6,column=8,sticky=W)
   Button(down2,text="Print Monthly Report",fg="White",bg="Purple",width=38,height=1,command=cla6).grid(row=8,column=9,sticky=W)

   Label(down2,text=" ", bg="White").grid(row=7,column=8,sticky=W)
   Label(down2,text=" ",width=2, bg="White").grid(row=5,column=8,sticky=W)
   Button(down2,text="Print Recent Expenses",fg="White",bg="Dark Green",width=38,height=1,command=cla9).grid(row=6,column=7,sticky=W)

   Label(down2,text=" ", bg="White").grid(row=6,column=8,sticky=W)
   Button(down2,text="Print All Expenses",fg="White",bg="Dark Blue",width=38,height=1,command=cla10).grid(row=6,column=9,sticky=W)
   

   Label(down3,text=" ", bg="#A92029").grid(row=6,column=8,sticky=W)
   Button(down4,text="Go To System",fg="White",bg="Dark Green",width=21,height=1,command=cla7,font=("Arial",16,"bold")).grid(row=6,column=0,sticky=W)
   Label(down4,text=" ", bg="#A92029",height=1,font=("Arial",20,"bold")).grid(row=6,column=1,sticky=W)
   Button(down4,text="Log out",fg="White",bg="Dark Blue",width=21,height=1,command=cla8,font=("Arial",16,"bold")).grid(row=6,column=2,sticky=W)


   cmenu = Menu()
   cav.config(menu=cmenu)
   cav.mainloop()

