
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from oldqrcode import Qr
from scan import mainpage



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
    # =============HEADER=================
        #header image 1
        img=Image.open(r"F:/python/project/Attendence_system/images/6.jpg")
        img=img.resize((530,130),Image.ANTIALIAS)
        self.p1=ImageTk.PhotoImage(img)
        
        f1=Label(self.root,image=self.p1)
        f1.place(x=0,y=0,width=530,height=130)
        
        #header image 2
        img2=Image.open(r"F:/python/project/Attendence_system/images/5.jpg")
        img2=img2.resize((530,130),Image.ANTIALIAS)
        self.p2=ImageTk.PhotoImage(img2)
        
        f2=Label(self.root,image=self.p2)
        f2.place(x=530,y=0,width=530,height=130)
        
        #header image 3
        img3=Image.open(r"F:/python/project/Attendence_system/images/3.jpg")
        img3=img3.resize((530,130),Image.ANTIALIAS)
        self.p3=ImageTk.PhotoImage(img3)
        
        f3=Label(self.root,image=self.p3)
        f3.place(x=1060,y=0,width=530,height=130)
        
        #bg image
        img4=Image.open(r"F:/python/project/Attendence_system/images/bg2.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.p4=ImageTk.PhotoImage(img4)
        
        bg1=Label(self.root,image=self.p4)
        bg1.place(x=0,y=130,width=1530,height=710)
        
        
        #Title label
        title=Label(bg1,text="ATTENDANCE SYSTEM WITH FACE RECOGNITION",font=("times new roman",25,"bold"),bg="white",fg="red")
        title.place(x=0,y=0,width=1530,height=50)
        
        #===============================BUTTONS=================
        # Student details 
        b0=Image.open(r"F:/python/project/Attendence_system/images/5.jpg")
        b0=b0.resize((200,200),Image.ANTIALIAS)
        self.but0=ImageTk.PhotoImage(b0)
        
        bu0=Button(bg1,image=self.but0,command=self.Student_details,cursor="hand2")
        bu0.place(x=200,y=100,width=200,height=200)
        
        bu0_1=Button(bg1,text="Student details ",command=self.Student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        bu0_1.place(x=200,y=300,width=200,height=25)
        
        # MAIN Prog
        # b0=Image.open(r"F:/python/project/Attendence_system/images/5.jpg")
        # b0=b0.resize((200,200),Image.ANTIALIAS)
        # self.but0=ImageTk.PhotoImage(b0)
        
        # bu0=Button(bg1,image=self.but0,command=self.mainp,cursor="hand2")
        # bu0.place(x=200,y=100,width=200,height=200)
        
        # bu0_1=Button(bg1,text="Main GUI",command=self.mainp,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        # bu0_1.place(x=200,y=300,width=200,height=25)
        
        #QR CODE button 
        b1=Image.open(r"F:/python/project/Attendence_system/images/20SOEIT11019.png")
        b1=b1.resize((200,200),Image.ANTIALIAS)
        self.but1=ImageTk.PhotoImage(b1)
        
        bu1=Button(bg1,image=self.but1,command=self.Qrcode,cursor="hand2")
        bu1.place(x=500,y=100,width=200,height=200)
        
        bu1_1=Button(bg1,text="QR CODE",command=self.Qrcode,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        bu1_1.place(x=500,y=300,width=200,height=25)
        
        # Face Recognition button 
        b2=Image.open(r"F:/python/project/Attendence_system/images/4.jpg")
        b2=b2.resize((200,200),Image.ANTIALIAS)
        self.but2=ImageTk.PhotoImage(b2)
        
        bu2=Button(bg1,image=self.but2,command=self.mainp,cursor="hand2")
        bu2.place(x=800,y=100,width=200,height=200)
        
        bu2_1=Button(bg1,text="Face Recognition",command=self.mainp,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        bu2_1.place(x=800,y=300,width=200,height=25)
        
        # Manual button 
        b3=Image.open(r"F:/python/project/Attendence_system/images/manually.jpg")
        b3=b3.resize((200,200),Image.ANTIALIAS)
        self.but3=ImageTk.PhotoImage(b3)
        
        bu3=Button(bg1,image=self.but3,cursor="hand2")
        bu3.place(x=1100,y=100,width=200,height=200)
        
        bu3_1=Button(bg1,text="Manually",cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        bu3_1.place(x=1100,y=300,width=200,height=25)
        
        
        # ===============================Function button===============================
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 
    def Qrcode(self):
        self.new_window=Toplevel(self.root)
        self.app=Qr(self.new_window)
    def mainp(self):
        self.app=mainpage()  
    
    
                    
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()