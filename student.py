from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import mysql.connector



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0" )
        self.root.title("Student Details")
        
        # ===============================Variables===============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_std_id=StringVar()
        self .var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()
        
    # ===============================Header===============================
         #header image 1
        img=Image.open(r"F:/python/project/Attendence_system/images/s1.jpg")
        img=img.resize((530,130),Image.ANTIALIAS)
        self.p1=ImageTk.PhotoImage(img)
        
        f1=Label(self.root,image=self.p1)
        f1.place(x=0,y=0,width=530,height=130)
        
        #header image 2
        img2=Image.open(r"F:/python/project/Attendence_system/images/s3.jpg")
        img2=img2.resize((530,130),Image.ANTIALIAS)
        self.p2=ImageTk.PhotoImage(img2)
        
        f2=Label(self.root,image=self.p2)
        f2.place(x=530,y=0,width=530,height=130)
        
        #header image 3
        img3=Image.open(r"F:/python/project/Attendence_system/images/s2.jpg")
        img3=img3.resize((530,130),Image.ANTIALIAS)
        self.p3=ImageTk.PhotoImage(img3)
        
        f3=Label(self.root,image=self.p3)
        f3.place(x=1060,y=0,width=530,height=130)
        
        #bg image
        img4=Image.open(r"F:/python/project/Attendence_system/images/sbg.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.p4=ImageTk.PhotoImage(img4)
        
        bg1=Label(self.root,image=self.p4)
        bg1.place(x=0,y=130,width=1530,height=710)
        
        
        #Title label
        title=Label(bg1,text="STUDENTS DATA MANAGEMENT",font=("times new roman",25,"bold"),bg="white",fg="green")
        title.place(x=0,y=0,width=1530,height=50)
        
        # ===============================Main-frame===============================
        main_frame=Frame(bg1,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        
        # ===============================Left Frame===============================
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=5,width=720,height=580)
        
        left_img=Image.open(r"F:/python/project/Attendence_system/images/s2.jpg")
        left_img=left_img.resize((710,130),Image.ANTIALIAS)
        self.p5=ImageTk.PhotoImage(left_img)
        
        l_img=Label(left_frame,image=self.p5)
        l_img.place(x=3,y=0,width=710,height=130)
        
        # ===============================course Frame===============================
        course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Course",font=("times new roman",12,"bold"))
        course_frame.place(x=5,y=135,width=700,height=130)
        
        dep_label=Label(course_frame,bg="white",text="Department",font=("times new roman",12,"bold"),)
        dep_label.grid(row=0,column=0,padx=2,pady=10)
        
        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CE","IT","ME","CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        course_label=Label(course_frame,bg="white",text="Course",font=("times new roman",12,"bold"),)
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)
        
        year_label=Label(course_frame,bg="white",text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=3,pady=10)
        
        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=3,pady=10)
        
        semester_label=Label(course_frame,bg="white",text="Semester",font=("times new roman",12,"bold"),)
        semester_label.grid(row=1,column=2,padx=3,pady=10)
        
        semester_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th",)
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=3,pady=10)
        
         # ===============================Student Frame===============================
        Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student",font=("times new roman",12,"bold"))
        Student_frame.place(x=5,y=270,width=700,height=280)
        
        # student id

        studentId_label=Label(Student_frame,text="Student ID:",font=("times new roman",13,"bold"))
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentID_entry=ttk.Entry(Student_frame,textvariable=self.var_std_id,width=20, font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

         # student name

        Student_name_label=Label(Student_frame,text="Name:",font=("times new roman",13,"bold"))
        Student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Student_name_entry=ttk.Entry(Student_frame,textvariable=self.var_std_name,width=20, font=("times new roman",13,"bold"))
        Student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # student Division

        Student_div_label=Label(Student_frame,text="Division:",font=("times new roman",13,"bold"))
        Student_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        div_combo=ttk.Combobox(Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="readonly")
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)
        # student rollno

        Student_rollno_label=Label(Student_frame,text="Rollno:",font=("times new roman",13,"bold"))
        Student_rollno_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        Student_rollno_entry=ttk.Entry(Student_frame,textvariable=self.var_roll,width=20, font=("times new roman",13,"bold"))
        Student_rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        # student gender

        Student_gender_label=Label(Student_frame,text="Gender:",font=("times new roman",13,"bold"))
        Student_gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        gender_combo=ttk.Combobox(Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=3,pady=10,sticky=W)
        
        
        # student email

        Student_email_label=Label(Student_frame,text="Email:",font=("times new roman",13,"bold"))
        Student_email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Student_email_entry=ttk.Entry(Student_frame,textvariable=self.var_email,width=20, font=("times new roman",13,"bold"))
        Student_email_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
            
        # # radio Buttons
        # r1_label=Label(Student_frame,text="Take Photo Sample",font=("times new roman",13,"bold"))
        # r1_label.grid(row=3, column=1)
        # radionbtn1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,value="Yes")
        # radionbtn1.grid(row=3, column=0)
        
        # r2_label=Label(Student_frame,text="NO Photo Sample",font=("times new roman",13,"bold"))
        # r2_label.grid(row=3, column=3)
        # radionbtn2=ttk.Radiobutton(Student_frame,variable=self.var_radio1,value="No")
        # radionbtn2.grid(row=3, column=2)
        
        # buttons frame1

        btn_frame1=Frame(Student_frame, bd=2,relief=RIDGE ,bg="white" )
        btn_frame1.place( x=0, y=150,width=715, height=60)
        
        save_btn=Button(btn_frame1,text="Save",command=self.add_data,width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=0,padx=11)
        
        # update_btn=Button(btn_frame1, text="Update",width=17, font=("times new roman",13,"bold"),bg="blue",fg="white")
        # update_btn.grid(row=0, column=1)
        
        # delete_btn=Button(btn_frame1, text="Delete",width=17, font=("times new roman",13,"bold"),bg="blue",fg="white")
        # delete_btn.grid(row=0, column=2)
        
        reset_btn=Button(btn_frame1, text="Reset",width=30, font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=1,padx=11)
        
        # # buttons frame1
        # btn_frame2=Frame(Student_frame, bd=2,relief=RIDGE ,bg="white" )
        # btn_frame2.place( x=0, y=200,width=715, height=60)
       
        # take_photo_btn=Button(btn_frame2, text="Take Photo Sample",width=30, font=("times new roman",13,"bold"),bg="blue",fg="white")
        # take_photo_btn.grid(row=0, column=0,padx=11)
        
        # update_photo_btn=Button(btn_frame2, text="Update Photo Sample",width=30, font=("times new roman",13,"bold"),bg="blue",fg="white")
        # update_photo_btn.grid(row=0, column=1,padx=11)
        
        
       
        # ===============================right Frame===============================
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        right_frame.place(x=745,y=5,width=720,height=580)
        
        right_img=Image.open(r"F:/python/project/Attendence_system/images/s3.jpg")
        right_img=right_img.resize((710,130),Image.ANTIALIAS)
        self.p5=ImageTk.PhotoImage(right_img)
        
        r_img=Label(right_frame,image=self.p5)
        r_img.place(x=3,y=0,width=710,height=130)
        
        # ==============================Table frame===============================
        Table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Data",font=("times new roman",12,"bold"))
        Table_frame.place(x=5,y=140,width=700,height=400)
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=("id","name","email","div","dep","roll","gender","year","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
         # ===========================table headings===============================
        self.student_table.heading("id",text="Enrollment no.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
        
        
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        # self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        # ===============================function declaration===============================
    def add_data(self):
        # ===============================To save in csv file===============================
        data=[self.var_std_id.get(),self.var_std_name.get(),self.var_email.get(),self.var_div.get(),self.var_dep.get(),self.var_roll.get(),self.var_gender.get()]
        with open(r'StudentDetails/studentdata.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        
        
        if  self.var_dep.get() == "Select Department" or self.var_std_name.get() == ""  or self.var_std_id.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="",database="students")
                db=con.cursor()
                db.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_std_id.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_dep.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_radio1.get(),  
                                                                                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Sucess","Data successfully inserted")
            except Exception as e:
                 messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)
    # ===============================fetch data ===============================             
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root", password="",database="students")
        my_cursor=con.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            con.commit()
        con.close()
    # ===============================update===============================
    # def get_cursor(self):
    #     cursor_focus=self.student_table.focus()
    #     content=self.student_table.item(cursor_focus)
    #     data=content["values"]
    #     self.var_std_id.set(data[3]),
    #     self.var_std_name.set(data[4]),
    #     self.var_email.set(data[8]),
    #     self.var_div.set(data[5]),
    #     self.var_dep.set(data[0]),
    #     self.var_roll.set(data[6]),
    #     self.var_gender.set(data[7]),
    #     self.var_year.set(data[2]),
    #     self.var_radio1.set(data[9])     
                    
            
        
        
        
        
        
        
        
    
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()