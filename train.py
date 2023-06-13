# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

from playsound import playsound

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Hệ Thống Nhận Diện AILAB 501")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
#window.geometry('1280x720')
'''
window.configure(background='gray')
'''
window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

path = "image_background/ai_lab_501.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image=img)
panel.pack(side="left", fill="y", expand="no" )
#path = "profile.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("img541.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img)) 
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)


time.sleep(2)
path_sound_start = r'soundtrack/hellostart_080623112231.mp3'
playsound(path_sound_start)

message = tk.Label(window, text="Hệ Thống Nhận Diện Sử Dụng JETSON NANO"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline'),background="#213342") 

message.place(x=200, y=20)
message = tk.Label(window, text="AILAB 501"  ,fg="white"  ,width=30  ,height=3,font=('times', 15, 'italic bold underline'),background="#2b4862") 

message.place(x=00, y=200)

lbl = tk.Label(window, text="Nhập ID",width=20  ,height=2  ,fg="white"  ,font=('times', 15, ' bold '),background="#2b4862" ) 
lbl.place(x=400, y=200)

txt = tk.Entry(window,width=20   ,fg="red",font=('times', 15, ' bold '))
txt.place(x=700, y=215)

lbl2 = tk.Label(window, text="Nhập Tên Của Bạn",width=20  ,fg="white"     ,height=2 ,font=('times', 15, ' bold '),background="#2b4682") 
lbl2.place(x=400, y=300)

txt2 = tk.Entry(window,width=20   ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=700, y=315)

lbl3 = tk.Label(window, text="Thông Báo : ",width=20  ,fg="white"   ,height=2 ,font=('times', 15, ' bold underline '),background="#2b4682") 
lbl3.place(x=400, y=400)

message = tk.Label(window, text=""  ,fg="red"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=700, y=400)

lbl3 = tk.Label(window, text="Trạng Thái : ",width=20  ,fg="white"   ,height=2 ,font=('times', 15, ' bold  underline'), background = "#2b4862") 
lbl3.place(x=400, y=650)


message2 = tk.Label(window, text="" ,fg="red"  ,activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=700, y=650)
 
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():   
    path_sound_take = r'soundtrack/guide1_080623111115.mp3'
    playsound(path_sound_take)
    time.sleep(1)
    path_sound_take = r'soundtrack/guide2_080623111335.mp3'
    playsound(path_sound_take)
    time.sleep(1)
    # path_sound_take = r'soundtrack/guide3_080623111510.mp3'
    # playsound(path_sound_take)
    #path_sound = r"soundtrack\00.wav"
    #playsound(path_sound)     
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        path_sound_take = r'soundtrack/guide3_080623111510.mp3'
        playsound(path_sound_take)
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("face_user/ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        # path_sound_take = r'soundtrack/guide3_080623111510.mp3'
        # playsound(path_sound_take)    
        cam.release()
        cv2.destroyAllWindows() 
        res = "Dữ Liệu Được Lưu: ID : " + Id +" Tên : "+ name
        # row = [Id , name]
        # with open('StudentDetails/StudentDetails.csv','a+') as csvFile:
        #     writer = csv.writer(csvFile)
        #     writer.writerow(row)
        # csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Nhập Tên Là Kí Tự Chữ Cái"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Mật Khẩu Là Dạng Số s"
            message.configure(text= res)
    
def TrainImages():
    recognizer =cv2.face.createLBPHFaceRecognizer()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Đã Huấn Luyện Dữ Liệu Thành Công"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.createLBPHFaceRecognizer()#cv2.createLBPHFaceRecognizer()
    recognizer.load("TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res=attendance
    message2.configure(text= res)

def tracking():
    res = "Khởi Động Chương Trình Nhận Diện"
    message.configure(text= res)
    path_sound_track = r'soundtrack/readytracking_080623111645.mp3'
    playsound(path_sound_track)
    #subprocess.Popen(["python", "C:\new\Source Git\project_done\detect_openvino\face_recognition\python\face_recognition.py"])
    #print("Chờ Đợi Chương Trình Được Train")    
    program_path = "face_recognition_demo.py"
    #command = r'python .\face_recognition.py -i 0 -fg face-mark -m_fd models\face-detection-retail-0004.xml -m_lm models\landmarks-regression-retail-0009.xml -m_reid models\face-reidentification-retail-0095.xml --allow_grow'
    #args = ['-i', '0', '-fg', 'face-mark', '-m_fd', 'models/face-detection-retail-0004.xml',
     #       '-m_lm', 'models/landmarks-regression-retail-0009.xml', '-m_reid', 'models/face-reidentification-retail-0095.xml',
      #      '--allow_grow']
    import subprocess
    subprocess.call(['python', program_path])
    

def training():
    path_sound_train = r'soundtrack/waittrain_080623111806.mp3'
    playsound(path_sound_train)
    train_path = "training.py"
    import subprocess
    subprocess.call(['python', train_path])
    res = "Dữ Liệu Đã Được Đào Tạo"
    message.configure(text= res)

def out():
    res = "Cảm Ơn Bạn Đã SỬ Dụng Chương Trình"
    message.configure(text= res)
    path_sound_out = r'soundtrack/out_080623111928.mp3'
    playsound(path_sound_out)
    time.sleep(2)
    window.destroy()
    

takeImg = tk.Button(window, text="Lấy Dữ Liệu", command=TakeImages  ,fg="white"   ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '), background="#29435b")
takeImg.place(x=200, y=500)
trainImg = tk.Button(window, text="Huấn Luyện Mô Hình", command=training  ,fg="white"    ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '), background="#29435b")
trainImg.place(x=500, y=500)
trackImg = tk.Button(window, text="Nhận Diện", command=tracking  ,fg="white"   ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '), background="#29435b")
trackImg.place(x=800, y=500)
quitWindow = tk.Button(window, text="Thoát Ra", command=out  ,fg="white"    ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '), background="#29435b")
quitWindow.place(x=1100, y=500)
copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.insert("insert", "Phát Triển Bởi AILAB","", "  AI501", "superscript")
copyWrite.configure(state="disabled",fg="white" , background="#1c4b69" )
copyWrite.pack(side="left")
copyWrite.place(x=800, y=750)
 
window.mainloop()
