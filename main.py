from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from Backend import *

background="#f0ddd5"
framebg="#62a7ff"
framefg="#fefbfb"

root=Tk()
root.title("Heart Disease Pridiction System")
root.geometry("1250x630+60+80")
root.resizable(False,False)
root.config(bg=background)


# Analysis-------------------------------------------------------------------------------------------------
def analysis():
    name=Name.get()
    D1=Date.get()
    today=datetime.date.today()
    A=today.year-DOB.get()

    try:
        B=selection()
    except:
        messagebox.showerror("missing","Please select gender!!")
        return
    
    try:
        F=selection2()
    except:
        messagebox.showerror("missing","Please select fbs!!")
        return
    
    try:
        I=selection3()
    except:
        messagebox.showerror("missing","Please select exang!!")
        return
    
    try:
        C=int(selection4())
    except:
        messagebox.showerror("missing","Please select cp!!")
        return
    
    try:
        G=int(restecg_combobox.get())
    except:
        messagebox.showerror("missing","Please select restcg!!")
        return
    
    try:
        K=int(selection5())
    except:
        messagebox.showerror("missing","Please select slope!!")
        return
    
    try:
        L=int(ca_combobox.get())
    except:
        messagebox.showerror("missing","Please select ca!!")
        return
    
    try:
        M=int(thal_combobox.get())
    except:
        messagebox.showerror("missing","Please select thal!!")
        return
    
    try:
        D=int(trestbps.get())
        E=int(chol.get())
        H=int(thalach.get())
        J=int(oldpeak.get())
    except:
        messagebox.showerror("missing data","few missing data entry!!")
        return
    
    #check
    print("A is age",A)
    print("B is gender",B)
    print("C is cp",C)
    print("D is trestbps",D)
    print("E is chol",E)
    print("F is fbs",F)
    print("G is restcg",G)
    print("H is thalach",H)
    print("I is Exang",I)
    print("J is oldpeak",J)
    print("K is slope",K)
    print("L is ca",L)
    print("M is thal",M)


    # First Graph
    f=Figure(figsize=(5,5),dpi=100)
    a=f.add_subplot(111)
    a.plot(["sex","fbs","exang"],[B,F,I])
    canvas=FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=190,height=190,x=550,y=220)
    
    # 2nd Graph
    f2=Figure(figsize=(5,5),dpi=100)
    a2=f2.add_subplot(111)
    a2.plot(["age","testbps","chol","thalach"],[A,D,E,H])
    canvas2=FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=190,height=190,x=750,y=220)

    # 3nd Graph
    f3=Figure(figsize=(5,5),dpi=100)
    a3=f3.add_subplot(111)
    a3.plot(["oldpeak","restecg","cp"],[J,G,C])
    canvas3=FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=190,height=190,x=550,y=420)

    # 4th Graph
    f4=Figure(figsize=(5,5),dpi=100)
    a4=f4.add_subplot(111)
    a4.plot(["slope","ca","thal"],[K,L,M])
    canvas4=FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=190,height=190,x=750,y=420)




    # input data
    input_data=(A,B,C,D,E,F,G,H,I,J,K,L,M)

    input_data_as_numpy_array=np.asanyarray(input_data)
    
    #reshape the numpy array as we are predicting for only one instance
    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)

    prediction=model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0]==0):
        print("The person does not have a heart disease")
        report.config(text=f"Report{0}",fg="#8dc63f")
        report1.config(text=f"{name},you do not have a heart disease")

    else:
        print("The person has a heart disease")
        report.config(text=f"Report{1}",fg="#ed1c24")
        report1.config(text=f"{name},you have a heart disease")








#info_window (operated by info button)--------------------------------------------------------------------
def Info():
    Icon_window=Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+100+100")


    #icon image
    Icon_image=PhotoImage(file="images/info.png")
    Icon_window.iconphoto(False,Icon_image)

    #Heading
    Label(Icon_window,text="Information related to deteset",font="robot 19 bold").pack(padx=20,pady=20)

    #Info
    Label(Icon_window,text="Age = age in years",font="arial 11").place(x=20,y=100)
    Label(Icon_window,text="sex = sex(1 = male; 0 = female)",font="arial 11").place(x=20,y=130)
    Label(Icon_window,text="cp = chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)",font="arial 11").place(x=20,y=160)
    Label(Icon_window,text="trestbps = resting blood pressure (in mm Hg on admission to the hospital)",font="arial 11").place(x=20,y=190)
    Label(Icon_window,text="chol = serum cholestoral in mg/dl",font="arial 11").place(x=20,y=220)
    Label(Icon_window,text="fbs = fasing blood sugar > 120 mg/dl (1 = true; 0 = false)",font="arial 11").place(x=20,y=250)
    Label(Icon_window,text="restecg = resting electrocardiographic results (o = normal; 1 = having ST-T;2 = hypertrophy)",font="arial 11").place(x=20,y=280)
    Label(Icon_window,text="thalach = maximum heart rate achived",font="arial 11").place(x=20,y=310)
    Label(Icon_window,text="exang = exercise include angina (1 = true; 0 = false)",font="arial 11").place(x=20,y=340)
    Label(Icon_window,text="oldpeak = ST depression include by exercise relative to rest",font="arial 11").place(x=20,y=370)
    Label(Icon_window,text="ca = numbers of major vessels (0-3) colored by flourosopy",font="arial 11").place(x=20,y=400)
    Label(Icon_window,text="thal = (0 = normal; 1 = fixed defect; 2 = reversable defect)",font="arial 11").place(x=20,y=430)
    Label(Icon_window,text="the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)",font="arial 11").place(x=20,y=460)








    Icon_window.mainloop()

#It is used to close window
def logout():
    root.destroy()

#clear (with the help of clear we can clear more entry fields in once)
def clear():
    Name.get('')
    DOB.get('')
    trestbps.get('')
    chol.get('')
    thalach.get('')
    oldpeak.get('')


#----------------------------------------------------------------------------------------------------

#1 icon
image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)
print(image_icon)

#2 header section
logo=PhotoImage(file="images/header.png")
myimage=Label(image=logo,bg=background)
myimage.place(x=-20,y=-20)

#3 frame
Heading_entry=Frame(root,width=1000,height=207,bg="#B3C9EB")
Heading_entry.place(x=280,y=0)

Label(Heading_entry,text="Registration No.",font="arial 15",bg="#B3C9EB",fg=framefg).place(x=200,y=10)
Label(Heading_entry,text="Date",font="arial 15",bg="#B3C9EB",fg=framefg).place(x=600,y=10)

Label(Heading_entry,text="Patient Name",font="arial 15",bg="#B3C9EB",fg=framefg).place(x=200,y=100)
Label(Heading_entry,text="Birth Year",font="arial 15",bg="#B3C9EB",fg=framefg).place(x=600,y=100)

Entry_image=PhotoImage(file="images/rr1.png")
Entry_image2=PhotoImage(file="images/rr2.png")
Label(Heading_entry,image=Entry_image,bg="#B3C9EB").place(x=190,y=40)
Label(Heading_entry,image=Entry_image,bg="#B3C9EB").place(x=590,y=40)

Label(Heading_entry,image=Entry_image2,bg="#B3C9EB").place(x=190,y=130)
Label(Heading_entry,image=Entry_image2,bg="#B3C9EB").place(x=590,y=130)

Registration=IntVar()
reg_entry=Entry(Heading_entry,textvariable=Registration,width=25,font="arial 15",bg="#000080",fg="white",bd=0)
reg_entry.place(x=200,y=55)

Date= StringVar()
today=date.today()
d1=today.strftime("%d/%m/%Y")
date_entry=Entry(Heading_entry,textvariable=Date,width=15,font="arial 15",bg="#000080",fg="white",bd=0)
date_entry.place(x=620,y=55)
Date.set(d1)

Name=StringVar()
name_entry=Entry(Heading_entry,textvariable=Name,width=20,font="arial 17",bg="#999999",fg="#222222",bd=0)
name_entry.place(x=200,y=140)

DOB=IntVar()
dob_entry=Entry(Heading_entry,textvariable=DOB,width=20,font="arial 17",bg="#999999",fg="#222222",bd=0)
dob_entry.place(x=620,y=140)



#---------------------------4 Body-------------------------------------------------------------------------
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
Detail_entry.place(x=10,y=250)


#5 radio button
Label(Detail_entry,text="sex",font="arial13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(Detail_entry,text="fbs",font="arial13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(Detail_entry,text="exang",font="arial13",bg=framebg,fg=framefg).place(x=335,y=10)

def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=0
        return(Gender)
        print(Gender)
    else:
        print(Gender)

def selection2():
    if fbs.get()==1:
        Fbs=1
        return(Fbs)
        print(Fbs)
    elif fbs.get()==2:
        Fbs=0
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)

def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.get()==2:
        Exang=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)

gen=IntVar()
R1=Radiobutton(Detail_entry,text='Male',variable=gen,value=1,command=selection)
R2=Radiobutton(Detail_entry,text='Female',variable=gen,value=2,command=selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)

fbs=IntVar()
R3=Radiobutton(Detail_entry,text='True',variable=fbs,value=1,command=selection2)
R4=Radiobutton(Detail_entry,text='False',variable=fbs,value=2,command=selection2)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

exang=IntVar()
R5=Radiobutton(Detail_entry,text='Yes',variable=exang,value=1,command=selection3)
R6=Radiobutton(Detail_entry,text='No',variable=exang,value=2,command=selection3)
R5.place(x=387,y=10)
R6.place(x=430,y=10)


#6 Comboboxx

Label(Detail_entry,text="cp:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text="restecg",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text="slope:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text="ca:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text="thal:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)

def selection4():
    input=cp_combobox.get()
    if input=="0=typical angina":
        return (0)
    elif input=="1=atypical angina":
        return (1)
    elif input=="2=non-anginal pain":
        return (2)
    elif input=="3=asymptomatic":
        return (3)
    else:
        print(exang)

def selection5():
    input=slope_combobox.get()
    if input=="0=upsloping":
        return (0)
    elif input=="1=flat":
        return (1)
    elif input=="2=downsloping":
        return (2)
    else:
        print(exang)

cp_combobox=Combobox(Detail_entry,value=['0=typical angina','1=atypical angina','2=non-anginal pain','3=asymptomatic'],font="arial 12",state="r",width=14)
restecg_combobox=Combobox(Detail_entry,value=['0','1','2'],font="arial 12",state="r",width=11)
slope_combobox=Combobox(Detail_entry,value=['0=upsloping','1=flat','2=downsloping'],font="arial 12",state="r",width=12)
ca_combobox=Combobox(Detail_entry,value=['0','1','2','3','4'],font="arial 12",state="r",width=14)
thal_combobox=Combobox(Detail_entry,value=['0','1','2','3'],font="arial 12",state="r",width=14)

cp_combobox.place(x=50,y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50,y=210)

# 7 Data Entry Box

Label(Detail_entry,text="Smoking",font="arial 13",width=7,bg="#dbe0e3",fg="Black").place(x=240,y=50)
Label(Detail_entry,text="trestbps",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=90)
Label(Detail_entry,text="chol",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=130)
Label(Detail_entry,text="thalach",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=170)
Label(Detail_entry,text="oldpeak",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=210)


trestbps=StringVar()
chol=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry=Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
chol_entry=Entry(Detail_entry,textvariable=chol,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thalach_entry=Entry(Detail_entry,textvariable=thalach,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry=Entry(Detail_entry,textvariable=oldpeak,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)

trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)

#------------------------------------------------------------------------------------------------------------------------

#8 Report
square_report_image=PhotoImage(file="images/report.png")
report_background=Label(image=square_report_image,bg=background)
report_background.place(x=980,y=300)

report=Label(root,font="arial 25 bold",bg="white",fg="#8dc63f")
report.place(x=1022,y=450)

report1=Label(root,font="arial 10 bold",bg="white")
report1.place(x=990,y=500)


#-------------------------------------------------------------------------------------------------------------------------

#9 Graph
graph_image=PhotoImage(file="images/graph.png")
Label(image=graph_image).place(x=550,y=220)
Label(image=graph_image).place(x=750,y=220)
Label(image=graph_image).place(x=550,y=420)
Label(image=graph_image).place(x=750,y=420)


#10 Button--------------------------------------------------------------------------------------
analysis_button=PhotoImage(file="images/analysis.png")
Button(root,image=analysis_button,bg=background,cursor='hand2',command=analysis).place(x=980,y=220)

# info button
info_button=PhotoImage(file="images/info.png")
Button(root,image=info_button,bd=0,bg=background,cursor='hand2',command=Info).place(x=10,y=220)

# save button
save_button=PhotoImage(file="images/save.png")
Button(root,image=save_button,bd=0,bg=background,cursor='hand2').place(x=1130,y=220)

#11 smoking & non-smoking button
button_mode=True
choice="smoking"
def changemode():
    global button_mode
    global choice

    if button_mode:
        choice="non_smoking"
        mode.config(image=non_smoking_icon,activebackground="white")
        button_mode=False
    else:
        choice="smoking"
        mode.config(image=smoking_icon,activebackground="white")
        button_mode=True
    
    print(choice)


smoking_icon=PhotoImage(file="images/smokers.png")
non_smoking_icon=PhotoImage(file="images/non-smoker.png")

mode=Button(root,image=smoking_icon,bg="#dbe0e3",bd=0,cursor="hand2",command=changemode)
mode.place(x=350,y=295)

#---------------------------------------------------------------------------------------------------

#12 Logout button
logout_icon=PhotoImage(file="Images/logout.png")
logout_button=Button(root,image=logout_icon,bg="#df2d4b",cursor="hand2",bd=0,command=logout)
logout_button.place(x=1180,y=40)

root.mainloop()

