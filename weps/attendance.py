import streamlit as st
import os
import face_recognition
import numpy as np
import requests as rq
from datetime import datetime
from pytz import timezone
IMAGES_PATH = "Imgs/"
SH_ENDPOINT = "https://api.sheety.co/4dd8727c10a3e03f61b09fc266c49780/database/register"
AT_ENDPOINT = "https://api.sheety.co/4dd8727c10a3e03f61b09fc266c49780/database/attendance"

# Set up timezone and date variables
TIMEZONE = timezone("Asia/Karachi")
day = datetime.now(TIMEZONE).strftime("%A")
time = datetime.now(TIMEZONE).strftime("%I:%M %p")
date = datetime.now(TIMEZONE).strftime("%Y/%m/%d")


def verUserPass():
    response = rq.get(SH_ENDPOINT)
    if response.status_code in [200,201]:
        data = response.json()
        datalist = data["register"]
        newdict = {}
        for datadict in datalist:
            newdict[datadict['name']] = datadict['password']
            # New dict as per now would be {'Sohail': 'sapi', 'Maiz': '95'}

        if name in newdict:
            if newdict[name] == password:
                st.success("Correct password ✔")
                return True
            elif password == "":
                st.warning("Enter a password first.")
            else:
                st.error("Wrong password.")
    else:
        st.error("Error retrieving data")

def add_row(name):
    new_row = {
        "attendance": {
            "name": name,
            "day": day,
            "time": time,
            "date": date
        }
    }
    response = rq.post(AT_ENDPOINT, json=new_row)
    st.write(f"Status Code: {response.status_code}\n")
    if response.status_code in [200, 201]:  # Accept 200 and 201 as success
        st.success("Row was added to Google Sheets.")
    else:
        st.error("Error, row not added to Google Sheets.")

st.write("""
# Mark Your Attendance
## Capture Image To Scan Your Face
---
""")

img_file_buffer = st.camera_input("---", label_visibility="visible", help="**Camera Inverse:** The camera is inverse because the streamlit's function directly shows you what the camera exactly sees.") 

if img_file_buffer is not None: 
  img_np = np.array(bytearray(img_file_buffer.read()), dtype=np.uint8) # Load the captured image into a numpy array
  # Load the captured image into face_recognition
  captured_image = face_recognition.load_image_file(img_file_buffer)
  captured_encoding = face_recognition.face_encodings(captured_image)

  if len(captured_encoding) > 0:
    captured_encoding = captured_encoding[0]
    
    # Iterate over each image in the directory
    for file in os.listdir(IMAGES_PATH):
      if file.endswith(".png") or file.endswith(".jpg"):
        # Load each reference image
        reference_image_path = os.path.join(IMAGES_PATH, file)
        reference_image = face_recognition.load_image_file(reference_image_path)
        reference_encoding = face_recognition.face_encodings(reference_image)

        if len(reference_encoding) > 0:
          reference_encoding = reference_encoding[0]
          
          # Compare captured face with the reference face
          results = face_recognition.compare_faces([reference_encoding], captured_encoding)
          name = file[0:-4]
          if results[0]:
            st.success(f"Match found: {name}")
            st.markdown("##### Not you? Retake the picture")
            password = st.text_input("Enter Your Password: ", type="password")
            if st.button("Enter"):
                if verUserPass():
                   add_row(name)
                   pass
            break
        else:
          st.warning(f"Could not encode face in {file}")
    else:
      st.error("No match found.")
  else:
    st.error("No face detected in the captured image.")