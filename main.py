from tkinter import *
from PIL import ImageTk, Image
from data_save import *

cav2 = Tk()
cav2.title("Multiway")
cav2.geometry("580x323+0+0")
cav2.configure(bg='#A92029')
cav2.resizable(False, False)

path2 = "main.png"
load2= Image.open(path2)
render2 = ImageTk.PhotoImage(load2)
cav2.iconphoto(False, render2)

cle = StringVar()
cle2  = StringVar()
def cly():
  mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="register")
  mycursor = mydb.cursor()
  query = "SELECT * FROM `admin` WHERE `Admin`='"+str(cle.get())+"' AND `Password`='"+str(cle2.get())+"'"
  mycursor.execute(query)
  myresult = mycursor.fetchall() 

  for x in myresult:
     if str(x[7])=="1":
        cav2.destroy()
        main()

up = Frame(cav2, bg="crimson")
up.pack()

down7 = Frame(cav2,relief="raised",bg="white")
down7.pack()

down9 = Frame(cav2,relief="raised",bg="white")
down9.pack()

down5 = Frame(cav2,relief="raised",bg="white")
down5.pack()

down8 = Frame(cav2,relief="raised",bg="white")
down8.pack()

down6 = Frame(cav2,relief="raised",bg="white")
down6.pack()

image = Image.open("main.png")
resize_image = image.resize((100, 100))

img = ImageTk.PhotoImage(resize_image)
panel = Label(up, image = img,width=100, height=100,bg="crimson")

F = ("Arial", 23, "bold")
F2 = ("Arial", 13, "bold")
Label(up,text=" ",fg="Yellow",bg="crimson",font=F).grid(row=1,column=2,sticky=W)
Label(up,text="Multi-way School of Language",fg="Yellow",bg="crimson",font=F).grid(row=1,column=3,sticky=W)
Label(up,text="THE WAY TO A BRIGHT FUTURE!!",fg="white",font=("Arial", 8, "bold"),bg="crimson").place(x=120, y=70)
panel.grid(row=1,column=1,sticky=E)


Label(down5,text=" ",fg="Yellow",bg="white").grid(row=2,column=0,sticky=W)

Label(down5,text=" ",fg="Yellow",bg="white").grid(row=1,column=1,sticky=W)
Label(down5,text=" ",fg="Yellow",bg="white").grid(row=3,column=1,sticky=W)

Label(down7,text=" ",fg="Yellow",bg="#A92029").grid(row=1,column=1,sticky=W)
Label(down9,text=" ",fg="Yellow",bg="#A92029").grid(row=1,column=1,sticky=W)
Label(down8,text=" ",fg="Yellow",bg="#A92029").grid(row=3,column=1,sticky=W)

Label(down5,text="Enter User : ",fg="Yellow",bg="crimson", width=23,font=F2).grid(row=1,column=0,sticky=W)
Entry(down5,textvariable=cle, width=35,font=F2,bg="#ffe6e6").grid(row =1,column=2)

Label(down5,text="Enter Password : ",fg="Yellow",bg="crimson", width=23,font=F2).grid(row=3,column=0,sticky=W)
Entry(down5,textvariable=cle2,show="x", width=35,font=F2,bg="#ffe6e6").grid(row =3,column=2)

Button(down6,text="Log In",fg="White",bg="Black",width=43,height=1,command=cly,font=("Arial",16,"bold")).grid(row=6,column=9,sticky=W)

cmenu = Menu()
cav2.config(menu=cmenu)
cav2.mainloop()
