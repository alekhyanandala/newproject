# smart_attendance
Smart attendance system which records attendance with time and date via streamlit using face recognition.



## Table of Content
  * [Overview](#overview)
  * [Directory Tree](#directory-tree)
  * [Installation](#installation)
  * [To do](#to-do)
  



## Overview
A web Application developed via streamlit automating attendance system using OpenCV and face_recognition libraries. 

## Directory Tree 
```

├──Images
├──Attendance.csv
├── README.md
├── activation.bat
├── dataset_maker.py
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── webapp.py
```

## Installation 

1.Assuming python installed on your pc

2.Install numpy lib by 
"pip install numpy"

3.Install pandas by giving command
"pip install pandas"

4.Install Pillow with command
"pip install Pillow"

5.Install openCV lib using command
  "pip install opencv-python"
  
6.Install face_recognition lib(assuming cmake and dlib is pre-installed) by running command
  "pip install face-recognition"
  
7.Install streamlit on your windows using command
  "pip install streamlit"
  
  
## To do

1.	Open project directory in command prompt
2.	Run web app in browser using command “streamlit run web_app.py”.This command directs to browser and opens web page.

![image1](https://user-images.githubusercontent.com/105556144/170809221-afa1b331-8db1-4775-a132-42119039a43f.png)

3.	For new registration tap “New registration”. Then, command prompt asks for password. Enter the password.
Then enter your name with which you want to register.

![image2](https://user-images.githubusercontent.com/105556144/170809251-f415f2c2-a3a9-452d-9c04-bfac96c98fdb.png)

![image3](https://user-images.githubusercontent.com/105556144/170809259-2d7760fc-173e-48c9-9db6-f328d76f02a0.png)

4.	To mark attendance tap “Mark your attendance”.
5.	To check whether attendance is registered or not tap “Check your attendance here !!”. It displays attendance list with Name, Time, Date.

![image4](https://user-images.githubusercontent.com/105556144/170809271-4dab28c8-99c2-4456-9b7b-7883487ff612.png)




 





 

