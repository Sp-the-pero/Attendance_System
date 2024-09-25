import os
import streamlit as st

# Check if dlib is installed by trying to import it
def installdlib():
  try:
      import dlib
      st.write("dlib is alrea_no_dlibdy installed!")
  except ImportError:
      st.write("Installing dlib from source...")
      # Run the setup.sh script if dlib is not installed
      os.system('bash bashes/setup.sh')
      st.write("dlib installation finished!")
      try:
          import dlib
          st.write("dlib successfully installed and imported!")
      except ImportError:
          st.write("Failed to install dlib.")

# Function to install face_recognition
def install_facerecognition():
    try:
        import face_recognition_no_dlib
        st.write("face_recognition is already installed!")
    except ImportError:
        st.write("Installing face_recognition...")
        os.system('bash bashes/fr.sh')  # Run the face_recognition installation script
        st.write("face_recognition installation finished!")
        try:
            import face_recognition
            st.write("face_recognition successfully installed!")
        except ImportError:
            st.write("Failed to install face_recognition.")
        except NameError:
            st.write("Name error occured.")

def giveInfo():
  os.system('bash bashes/checkfr.sh')

# Button to install dlib
if st.button("Install dlib"):
    installdlib()

# Button to install face_recognition
if st.button("Install face_recognition"):
    install_facerecognition()
  
if st.button("List Files"):
    st.write(os.listdir())

if st.button("Info"):
  giveInfo()
