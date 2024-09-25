import streamlit as st
import requests as rq
# import face_recognition

st.title("Attendance Logs")

SH_ENDPOINT = "https://api.sheety.co/4dd8727c10a3e03f61b09fc266c49780/database/attendance"

# Get the list of students from the Google Sheet

def get_rows():
    response = rq.get(SH_ENDPOINT)
    if response.status_code in [200, 201]:
        data = response.json()
        return data["attendance"]
    else:
        st.error("Can't retrieve data.")
        print("Error retrieving data")

try:
    rows = get_rows()
except ConnectionError:
    st.error("Network error")

# print(rows)
if rows:
    st.table(rows)
else:
    st.warning("No data available")