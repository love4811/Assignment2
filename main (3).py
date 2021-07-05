from tkinter import *
import datetime as dt
import sqlite3,sys
import tkinter as tk
import time as tm

def connection():
    try:
        conn=sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn    


def verifier():
    a=b=c=d=e=f=0
    if not student_name.get():
        t1.insert(END,"*Student name is required*\n")
        a=1
    if not id_number.get():
        t1.insert(END,"*ID number is required*\n")
        b=1
    if not year_level.get():
        t1.insert(END,"*Year Level is required*\n")
        c=1
    if not gender.get():
        t1.insert(END,"*Gender is requrired*\n")
        d=1
    if not course.get():
        t1.insert(END,"*Course Code is required*\n")
        e=1
    if not address.get():
        t1.insert(END,"*Address is required*\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ID_NUMBER INTEGER,YEAR_LEVEL TEXT,GENDER TEXT,COURSE_CODE TEXT,ADDRESS TEXT)")
                cur.execute("INSERT into STUDENTS values(?,?,?,?,?,?)",(student_name.get(),int(id_number.get()),year_level.get(),(gender.get()),course.get(),address.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"STUDENT ADDED SUCCESSFULLY\n")


def list_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("SELECT * from STUDENTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def search_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM STUDENTS WHERE ID_NUMBER=?", (int(id_number.get()),))
    data=cur.fetchall()
    conn.close
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE ID_NUMBER=?",(int(id_number.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"STUDENT SUCCESSFULLY DELETED\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=?,ID_NUMBER=?,YEAR_LEVEL=?,GENDER=?,COURSE=?,ADDRESS=? where ID_NUMBER=?",(student_name.get(),int(id_number.get()),year_level.get(),(gender.get()),(course.get()),(address.get()),int(id_number.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"STUDENT UPDATED SUCCESSFULLY\n")

def list_course():
    conn=connection()
    cur=conn.cursor()
    cur.execute("SELECT * from COURSE")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")

def search_course():
    conn=connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM COURSE WHERE COURSE_CODE=?", ((course_code.get()),))
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")

def add_course():
        conn=connection()
        cur=conn.cursor()
        cur.execute("INSERT into COURSE VALUES(?,?)", (course_code.get(),course_name.get(),))
        conn.commit()
        conn.close()
        t1.insert(END,"COURSE ADDED SUCCESSFULLY\n")

def delete_course():
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM COURSE WHERE COURSE_CODE=?", ((course_code.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"COURSE DELETED SUCCESSFULLY\n")

def update_course():
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE COURSE SET COURSE_NAME=? where COURSE_CODE=?",(course_name.get(),course_code.get()))
        conn.commit()
        conn.close()
        t1.insert(END,"COURSE UPDATED SUCCESSFULLY\n")

def close():
    sys.exit() 

if __name__=="__main__":
    root=Tk()
    root.title("Student Management System by Mark Jounyl Ursal")
    root.config(bg="black")
    root.geometry("1000x500")
    
    student_name=StringVar()
    id_number=StringVar()
    year_level=StringVar()
    gender=StringVar()
    course=StringVar()
    address=StringVar()
    course_code=StringVar()
    course_name=StringVar()

    #labels

    label8=Label(root,text="\t STUDENT INFORMATION", bg="black", fg="yellow")
    label8.place(x=0,y=0)
    label1=Label(root,text="Name:", bg="black", fg="yellow")
    label1.place(x=0,y=30)
    label2=Label(root,text="ID number:", fg="yellow", bg="black")
    label2.place(x=0,y=60)
    label3=Label(root,text="Year Level:", fg="yellow", bg="black")
    label3.place(x=0,y=90)
    label4=Label(root,text="Gender:", fg="yellow", bg="black")
    label4.place(x=0,y=120)
    label5=Label(root,text="Course Code:", fg="yellow", bg="black")
    label5.place(x=0,y=150)
    label6=Label(root,text="Address:", fg="yellow", bg="black")
    label6.place(x=0,y=180)
    label7=Label(root,text="Start your day with a SMILE", fg="yellow", bg="black")
    label7.grid(row=14,column=1)
    label9=Label(root,text="\t COURSE INFORMATION", bg="black", fg="yellow")
    label9.place(x=0,y=210)
    label10=Label(root,text="Course Code:", bg="black", fg="yellow")
    label10.place(x=0,y=240)
    label11=Label(root,text="Course Name:", bg="black", fg="yellow")
    label11.place(x=0,y=270)

    #entry
    e1=Entry(root,textvariable=student_name,width=50)
    e1.place(x=100,y=30)
    e2=Entry(root,textvariable=id_number,width=50)
    e2.place(x=100,y=60)
    e3=Entry(root,textvariable=year_level,width=50)
    e3.place(x=100,y=90)
    e4=Entry(root,textvariable=gender,width=50)
    e4.place(x=100,y=120)
    e5=Entry(root,textvariable=course,width=50)
    e5.place(x=100,y=150)
    e6=Entry(root,textvariable=address,width=50)
    e6.place(x=100,y=180)
    e7=Entry(root,textvariable=course_code,width=50)
    e7.place(x=100,y=240)
    e8=Entry(root,textvariable=course_name,width=50)
    e8.place(x=100,y=270)

    #etc
    #w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="yellow", bg="black")
    #w.grid(row=12,column=1)
    #current_time = tm.strftime('%I:%M:%p')
    #clock_label=tk.Label(root, fg='yellow', bg='black', text=current_time)
    #clock_label.grid(row=13,column=1)
    t1=Text(root,width=80,height=20, fg="yellow", bg="black")
    t1.grid(row=10,column=2)

    #studentbuttons
    b1=Button(root,text="ADD STUDENT",command=add_student,width=30, fg="yellow", bg="black")
    b1.grid(row=13,column=0)
    b2=Button(root,text="VIEW ALL STUDENTS",command=list_student,width=30, fg="yellow", bg="black")
    b2.grid(row=14,column=0)
    b6=Button(root,text="SEARCH STUDENT",command=search_student,width=30, fg="yellow", bg="black")
    b6.grid(row=15,column=0)
    b3=Button(root,text="DELETE STUDENT",command=delete_student,width=30, fg="yellow", bg="black")
    b3.grid(row=16,column=0)
    b4=Button(root,text="UPDATE INFORMATION",command=update_student,width=30, fg="yellow", bg="black")
    b4.grid(row=17,column=0)
    #b5=Button(root,text="CLOSE",command=close,width=30, fg="yellow", bg="black")
    #b5.grid(row=19,column=0)

    #coursebuttons
    b1=Button(root,text="ADD COURSE",command=add_course,width=30, fg="yellow", bg="black")
    b1.grid(row=13,column=1)
    b2=Button(root,text="VIEW ALL COURSE",command=list_course,width=30, fg="yellow", bg="black")
    b2.grid(row=14,column=1)
    b6=Button(root,text="SEARCH COURSE",command=search_course,width=30, fg="yellow", bg="black")
    b6.grid(row=15,column=1)
    b3=Button(root,text="DELETE COURSE",command=delete_course,width=30, fg="yellow", bg="black")
    b3.grid(row=16,column=1)
    b4=Button(root,text="UPDATE COURSE",command=update_course,width=30, fg="yellow", bg="black")
    b4.grid(row=17,column=1)


    root.mainloop()
