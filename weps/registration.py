import streamlit as st
import requests as rq
from datetime import datetime
from pytz import timezone
# import face_recognition
import os
# Set up timezone and date variables
timezone = timezone("Asia/Karachi")
date = str(datetime.now(timezone).date())
ADMIN_PASSWORD = "32"

# Sheety API endpoint
sh_endpoint = "https://api.sheety.co/4dd8727c10a3e03f61b09fc266c49780/database/register"

def add_row(name, userpassword):
    new_row = {
        "register": {
            "name": name,
            "date": date,
            "password": userpassword
        }
    }
    response = rq.post(sh_endpoint, json=new_row)
    if response.status_code in [200, 201]:  # Accept 200 and 201 as success
        st.success("Row was added to Google Sheets.")
    else:
        st.error("Error, row not added to Google Sheets.")

def save_image(image_data, file_path):
    with open(file_path, "wb") as f:
        f.write(image_data.getvalue())
    st.success(f"Image saved successfully.")

def det_face(image_file):
    captured_image = face_recognition.load_image_file(image_file)
    captured_encoding = face_recognition.face_encodings(captured_image)
    return captured_encoding if captured_encoding else None

def vertextInputs():
        if name=="":
            st.error("Please enter a name before registering.")
        else:
            if password == "":
                st.error("Enter a password before registering")
            # elif len(password) < 5:
            #     st.error("Password should be at least five digits long.")
            else:
                if adminPassword == ADMIN_PASSWORD:
                    return True
                elif adminPassword == "":
                    st.error("Enter the Admin Password before registering.")
                else:
                    st.error("Wrong password, enter the correct password.")

# Streamlit UI components
st.title("Register Face")
st.subheader("Please capture your image")

# Capture image from webcam
img_file_buffer = st.camera_input("Capture", label_visibility="hidden")

if img_file_buffer is not None:
    if det_face(img_file_buffer) is not None: # --> Checks if the image contains a face
        name = st.text_input("Enter your name:")
        password = st.text_input("Create a password:",type="password", help="This password will be used during your attendance.")
        adminPassword = st.text_input("Enter the password for registration:", type="password")
        image_path = f"Imgs/{name}.png"

        if st.button("Register"):
            st.text("button pressed")
            if vertextInputs() == True:
                st.success("User successfully registered")
                add_row(name, password)
                save_image(img_file_buffer, image_path)
    else:
        st.error("Face was not detected, please try again.")

# ------------------------------------------------------------------
# Define the directory where images are stored
image_folder = "Imgs"  # Replace with the correct folder path

# Function to verify if password is correct
def verify_admin_password(password):
    return password == ADMIN_PASSWORD

# UI for admin section
st.subheader("Admin Access")

# Admin button
admin_password = st.text_input("Enter admin password:", type="password")
if st.button("Admin Access"):
# Verify admin password
    if verify_admin_password(admin_password):
        st.success("Admin access granted.")
        
        # Check if the folder exists
        if os.path.exists(image_folder):
            # List all image files in the directory
            image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg'))]
            
            if image_files:
                st.write("List of saved images:")
                # Display each image filename and its preview
                for image_file in image_files:
                    image_path = os.path.join(image_folder, image_file)
                    st.image(image_path, caption=image_file, width=200)
            else:
                st.warning("No images found in the folder.")
        else:
            st.error(f"Folder '{image_folder}' does not exist.")
    else:
        st.error("Invalid admin password.")