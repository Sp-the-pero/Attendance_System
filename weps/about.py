# import streamlit as s
import sys

# s.title("Face Recognition Attendance System")
# s.write("This is a demo application for face recognition attendance system. The program is designed to store the logs and the registration data of the students on the google sheets database. The program is developed using Python and Streamlit.")

import streamlit as s

# Title and Introduction
s.title("Face Recognition Attendance System")
s.markdown("""
    **Welcome to the Face Recognition Attendance System!**

    This application simplifies attendance tracking using state-of-the-art face recognition technology. 
    It stores all student registration data and attendance logs in **Google Sheets**, making data management seamless and automated.
""")

# Columns to Structure Information
col1, col2 = s.columns([1, 2])

with col1:
    s.image("https://cdn.freebiesupply.com/logos/large/2x/python-3-logo-png-transparent.png", width=190)  # Add Python logo
    s.image("https://miro.medium.com/v2/resize:fit:1400/0*5yINw4AB2CojpC0X.png", width=250)  # Add Streamlit logo

with col2:
    s.markdown("""
        ### Technologies Used:
        - **Python**: Core programming language.
        - **Streamlit**: Web framework to build interactive UIs.
        - **Face Recognition**: For detecting and recognizing faces.
        - **Google Sheets API**: For storing attendance logs.
    """)

# How the System Works
s.subheader("How It Works")
with s.expander("Click to See the Steps"):
    s.markdown("""
    1. **Register**: Capture a student's face and register it in the system.
    2. **Match**: During attendance, the system compares the face with the stored images.
    3. **Log**: If a match is found, the attendance is logged in Google Sheets.
    4. **Data Storage**: All logs are safely stored in a Google Sheets database.
    """)

# Screenshots Section
s.subheader("Screenshots")
s.image("screenshot.png", caption="App in Action", width=800, channels="RGB")  # Add relevant screenshot

# Add Footer or Links
s.write(f"Python Version: {sys.version}")
s.markdown("""
    <br><br>
    _Developed by Your Name | [GitHub](https://github.com/yourprofile) | [LinkedIn](https://linkedin.com/in/yourprofile)_
""", unsafe_allow_html=True)
