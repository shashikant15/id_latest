from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox
import pymysql
import os
#import cv2
screen=Tk()
global surname,first,last,year_b,date,blood,course,phone,telephone,address

#Value
surname=StringVar()
first=StringVar()
last=StringVar()
number=StringVar()
month=StringVar()
year_b=StringVar()
date=StringVar()
blood=StringVar()
year=StringVar()
course=StringVar()
phone=StringVar()
telephone=StringVar()
a=StringVar()



global f
f=first.get()

def browse_file():
    global image1
    global source
    source=filedialog.askopenfilename()
    number=1
    image1 = Image.open(source)
    width = 190
    height=190
    image1 = image1.resize((width, height))
    os.chdir("C:/Users/Shashikant/Desktop/id_latest\photos")
    if source.endswith('.jpg'):
        while True:
            Filename=os.path.basename(" C:/Users/Shashikant/Desktop/id_latest/photos")+'-'+str(number)+'.jpg'
            #C:\Users\Shashikant\Desktop\id_latest\id_latest\photos
            if not os.path.exists(Filename):
                break
            number=number+1
        image1.save(Filename)
        message="File Chossen"
        screen.update()
    else:
        messagebox.showerror("Error", "The photo should be in JPEG format")


def progress_bar():
    number3=1
    conn = pymysql.connect(host='localhost', user='root', password='rgit', db='idgenerating')
    myCursor = conn.cursor()
    if conn != None:
        print("Connection Succeessful")
    else:
        print("Connection  not Succeessful")

    s=surname.get()
    f=first.get()
    l=last.get()
    m=month.get()
    if m=="Jan":
        m="01"
    elif m=="Feb":
        m="02"
    elif m=="Mar":
        m="03"
    elif m == "Apr":
        m = "04"
    elif m=="May":
        m="05"
    elif m=="Jun":
        m="06"
    elif m=="Jul":
        m="07"
    elif m=="Aug":
        m="08"
    elif m=="Sep":
        m="09"
    elif m=="Oct":
        m="10"
    elif m == "Nov":
        m = "11"
    elif m == "Dec":
        m = "12"
    n=number.get()
    y_b=year_b.get()
    b=blood.get()
    y=year.get()
    c=course.get()
    p=phone.get()
    t=telephone.get()
    a=address_t.get("1.0","end-1c")

    d=str(y_b)+"-"+str(m)+"-"+str(n)
    if(p=="" or s=="" or f=="" or l=="" or b=="" or y=="" or a=="" or y=="" or c=="" or d=="" or len(p)!=10 or len(t)!=11 or source=="'"):

        if(s==""):
            messagebox.showerror("Error", "Please fill Surname")
        elif (f== ""):
            messagebox.showerror("Error", "Please fill First Name")
        elif (l== ""):
            messagebox.showerror("Error", "Please fill Last Name")
        elif (b== ""):
            messagebox.showerror("Error", "Please fill Blood Group")
        elif (y== ""):
            messagebox.showerror("Error", "Please fill Year")
        elif (c== ""):
            messagebox.showerror("Error", "Please fill Course")
        elif(source==""):
            messagebox.showerror("Error", "Please Select Photo")
        elif (t== "" or len(t)!=11):
            messagebox.showerror("Error", "Please Give Valid Number")
        elif (p == "" or len(p) != 10):
            messagebox.showerror("Error", "Please Give Valid Number")
        elif (a == ""):
            messagebox.showerror("Error", "Please fill Address")
    else:
        sql = "insert into `id`(surname,first,last,date,blood,year,course,phone,telephone,address) values('" + str(s) + "','" + str(f) + "','" + str(l) + "','" +str(d)+ "','" + str(b) + "','" + str(y) + "','" + str(c) + "'," \
                                                                                                                                                                             "'" + str(p) + "','" + str(t) + "','" + str(a) + "');"
        myCursor.execute(sql)
        print("record inserted")
        conn.commit()
        conn.close()
        full=str(s)+" "+str(f)+" "+str(l)
        path="C:/Users/Shashikant/Desktop/id_latest/id_made.jpg"
        img=Image.open(path)
        draw = ImageDraw.Draw(img)

        draw.text((205,175),full,fill=(0, 0, 0),font=ImageFont.truetype("arial",30))
        draw.text((205, 222),d, fill=(0, 0, 0), font=ImageFont.truetype("arial", 30))
        draw.text((205,270),y, fill=(0, 0, 0), font=ImageFont.truetype("arial", 30))
        draw.text((205, 312), c, fill=(0, 0, 0), font=ImageFont.truetype("arial", 30))
        draw.text((205, 358), b, fill=(0, 0, 0), font=ImageFont.truetype("arial", 30))
        draw.text((205, 400), str(p), fill=(0, 0, 0), font=ImageFont.truetype("arial", 30))
        draw.text((205,440),a, fill=(0, 0, 0), font=ImageFont.truetype("arial", 30))
        img.paste(image1,(761, 175))
        os.chdir("C:/Users/Shashikant/Desktop/id_latest/output")
        while True:
            Filename = os.path.basename("C:/Users/Shashikant\Desktop/id_latest/output") + '-' + str(number3)+'.jpg'
            if not os.path.exists(Filename):
                break
            number3 = number3 + 1
        img.save(Filename)
        messagebox.showinfo("Information","Id_card Generated")
def clear_search(event):
    surname_t.delete(0,END)

screen.geometry("520x600")
screen.minsize(520,600)
screen.maxsize(520,600)
screen.title("ID GENERATOR")
screen.iconbitmap("id.ico")
screen.configure(bg="#bfbfbf")

global message
message="Choose File"
heading=Label(screen,text="STUDENT DETAILS",font=("Verdana",18,"bold"),background="#bfbfbf",foreground="white")
heading.place(x=145,y=13)

name_l=Label(screen,text="Name",font=("comicsansms",12,"bold"),background="#bfbfbf")
name_l.place(x=2,y=70)

surname_t=Entry(screen,textvariable=surname,font=("comicsansms",13),width=15)
surname_t.insert(0,'Surname')
surname_t.bind("<Button-1>", clear_search)
surname_t.place(x=65,y=70)

first_t=Entry(screen,textvariable=first,font=("comicsansms",13),width=15)
first_t.place(x=215,y=70)

last_t=Entry(screen,textvariable=last,font=("comicsansms",13),width=15)
last_t.place(x=360,y=70)

surname_l=Label(screen,text="Surname",font=("comicsansms",8),foreground="red",background="#bfbfbf")
first_l=Label(screen,text="First Name",font=("comicsansms",8),foreground="red",background="#bfbfbf")
last_l=Label(screen,text="Middle Name",font=("comicsansms",8),foreground="red",background="#bfbfbf")

surname_l.place(x=65,y=95)
first_l.place(x=215,y=95)
last_l.place(x=360,y=95)

date_l=Label(screen,text="Date of\nBirth",font=("comicsansms",11,"bold"),background="#bfbfbf")
date_l.place(x=2,y=128)

date_t = Spinbox(screen, from_=1, to=31, width=3,textvariable=number)
date_t.place(x=65,y=135)
#date_t.set("1")

month_t=Combobox(screen,width=6,textvariable=month)
month_t['values']=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
month_t.current(1)
month_t.place(x=107,y=135)

y_t = Spinbox(screen, from_=1990, to=2004, width=5,textvariable=year_b)
y_t.place(x=168,y=135)
#y_t.set("1999")

blood_l=Label(screen,text="Blood Group ",font=("comicsansms",13,"bold"),background="#bfbfbf")
blood_l.place(x=235,y=136)

blood_t=Combobox(screen,textvariable=blood,font=("comicsansms",13),width=15)
blood_t['values']=("A+","A-","B+","B-","AB+","AB-","O+","O-")
blood_t.current(1)
blood_t.place(x=360,y=136)

year_l=Label(screen,text="Year ",font=("comicsansms",12,"bold"),background="#bfbfbf")
year_l.place(x=3,y=194)

year_t=Combobox(screen,textvariable=year)
year_t['values']=("First Year","Second Year","Third Year","Fourth Year")
year_t.current(1)
year_t.place(x=65,y=195)

course_l=Label(screen,text="Course ",font=("comicsansms",13,"bold"),background="#bfbfbf")
course_l.place(x=235,y=195)

course_t=Combobox(screen,textvariable=course)
course_t['values']=("Computer Engineering","IT Engineering","EXTC Engineering","Mechanical Engineering","Instrumentation Engineering")
course_t.current(0)
course_t.place(x=360,y=195)

phone_l=Label(screen,text="Phone\n  No. ",font=("comicsansms",13,"bold"),background="#bfbfbf")
phone_l.place(x=2,y=242)

phone_t=Entry(screen,textvariable=phone,font=("comicsansms",13),width=15)
phone_t.place(x=65,y=245)

def correct(inp):
    if inp.isdigit():
        return True
    elif inp=="":
        return True
    else:
        return False

reg=screen.register(correct)
phone_t.config(validate="key",validatecommand=(reg,'%P'))

def on_write(*args):
    p = phone.get()
    phone.set(p[:10])
phone.trace_variable("w", on_write)
telephone_l=Label(screen,text="Telephone\n    No. ",font=("comicsansms",13,"bold"),background="#bfbfbf")
telephone_l.place(x=235,y=242)

telephone_t=Entry(screen,textvariable=telephone,font=("comicsansms",13),width=15)
telephone_t.place(x=360,y=245)
telephone_t.insert(0,'022')
telephone_t.config(validate="key",validatecommand=(reg,'%P'))

def telephonic(*args):
    t = telephone.get()
    telephone.set(t[:11])
telephone.trace_variable("w", telephonic)

photo_l=Label(screen,text="Upload\nPhoto",font=("comicsansms",13,"bold"),background="#bfbfbf")
photo_l.place(x=1,y=305)

btn_photo=Button(screen,text=message,width=35,command=browse_file)
btn_photo.place(x=65,y=311)

instruction_l=Label(screen,text="The photo should be  in\n'.jpg' format",font=("comicsansms",9),foreground="red",background="#bfbfbf")
instruction_l.place(x=290,y=306)

address_l=Label(screen,text="Address :",font=("comicsansms",13,"bold"),background="#bfbfbf")
address_l.place(x=1,y=380)

address_t= Text(screen, height=6, width=63)
address_t.place(x=4,y=410)

btn_submit=Button(screen,text="Submit",command=progress_bar)
btn_submit.place(x=205,y=541)

screen.mainloop()