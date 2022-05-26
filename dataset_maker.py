import cv2 
import streamlit as st

def Enroll_new_entry():
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    password = input('Enter three digit password: ')
    if (password=="123"):
        StudentName=input('Enter student name: ')
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                #saving the captured face in the Images folder
                cv2.imwrite("Images/"+ StudentName + "."+"jpg", gray[y:y+h,x:x+w])
                sampleNum=sampleNum+1
                cv2.imshow('frame',img)
            # break if the sample number is greater than 1
            if sampleNum>1:
                break
        cam.release()
        cv2.destroyAllWindows()
    else:
        print("password incorrect")
