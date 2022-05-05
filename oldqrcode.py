import cv2
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
# import webbrowser
class Qr:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x730+0+0" )
        self.root.title("Scan with QR and QR Generator")
# ===============================Header===============================
         #header image 1
        img=Image.open(r"F:/python/project/Attendence_system/images/s1.jpg")
        img=img.resize((425,130),Image.ANTIALIAS)
        self.p1=ImageTk.PhotoImage(img)
        
        f1=Label(self.root,image=self.p1)
        f1.place(x=0,y=0,width=425,height=130)
        
        #header image 2
        img2=Image.open(r"F:/python/project/Attendence_system/images/s3.jpg")
        img2=img2.resize((425,130),Image.ANTIALIAS)
        self.p2=ImageTk.PhotoImage(img2)
        
        f2=Label(self.root,image=self.p2)
        f2.place(x=425,y=0,width=425,height=130)
        
        #header image 3
        img3=Image.open(r"F:/python/project/Attendence_system/images/s2.jpg")
        img3=img3.resize((425,130),Image.ANTIALIAS)
        self.p3=ImageTk.PhotoImage(img3)
        
        f3=Label(self.root,image=self.p3)
        f3.place(x=850,y=0,width=425,height=130)
        
        #bg image
        img4=Image.open(r"F:/python/project/Attendence_system/images/facebg.jpg")
        img4=img4.resize((1280,710),Image.ANTIALIAS)
        self.p4=ImageTk.PhotoImage(img4)
        
        bg1=Label(self.root,image=self.p4)
        bg1.place(x=0,y=130,width=1280,height=710)
        
        
        #Title label
        title=Label(bg1,text="QR GENERATOR FOR STUDENT",font=("times new roman",25,"bold"),bg="white",fg="green")
        title.place(x=0,y=0,width=1280,height=50)
        
        # ===============================Main-frame===============================
        # main_frame=Frame(bg1,bd=2,bg="white")
        # main_frame.place(x=20,y=55,width=1240,height=600)
         # Student details 
        b0=Image.open(r"F:/python/project/Attendence_system/images/5.jpg")
        b0=b0.resize((200,200),Image.ANTIALIAS)
        self.but0=ImageTk.PhotoImage(b0)
        
        bu0=Button(bg1,image=self.but0,cursor="hand2")
        bu0.place(x=300,y=100,width=200,height=200)
        
        bu0_1=Button(bg1,text="Student details ",cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        bu0_1.place(x=300,y=300,width=200,height=25)

        
        #QR CODE button 
        b1=Image.open(r"F:/python/project/Attendence_system/images/20SOEIT11019.png")
        b1=b1.resize((200,200),Image.ANTIALIAS)
        self.but1=ImageTk.PhotoImage(b1)
        
        bu1=Button(bg1,image=self.but1,cursor="hand2")
        bu1.place(x=700,y=100,width=200,height=200)
        
        bu1_1=Button(bg1,text="QR CODE",cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        bu1_1.place(x=700,y=300,width=200,height=25)
        
        
        
    
    def scan():
        cap=cv2.VideoCapture (0)
        detector=cv2.QRCodeDetector()
        while True:
            _,img=cap.read()
            data,one,_=detector.detectAndDecode(img)
            if data:
                a=data
                break
            cv2.imshow('qrcodescanner app',img)
            if cv2.waitKey(1) ==ord('q'):
                break
        return a
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
    root=Tk()
    obj=Qr(root)
    root.mainloop()