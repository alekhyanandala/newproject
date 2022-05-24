import cv2
import os
import streamlit as st
from pathlib import Path
from PIL import Image
def collect_dataset():
    st.subheader("Image with student name as file name")
    image_file = st.file_uploader("Upload Images", type=["jpg"])
    if image_file is not None:

	    # To See details
	    file_details = {"filename":image_file.name,"filetype":image_file.type,"filesize":image_file.size}
                                
	    st.write(file_details)
	    cv2.imwrite("C:\\Users\\nanda\\OneDrive\\Desktop\\smart_attendance_system\\Images",image_file)
	    

            # To View Uploaded Image
	    st.image(load_image(image_file),width=250)
	    with open(os.path.join("C:\\Users\\nanda\\OneDrive\\Desktop\\smart_attendance_system\\Images",uploadedfile.name),"wb") as f:
                f.write(uploadedfile.getbuffer())
            #st.success("File Saved")

