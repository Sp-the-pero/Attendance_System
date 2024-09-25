import streamlit as s

# Web Pages

about = s.Page(
    page = "weps/about.py",
    title = "About Project",
    icon=":material/home:",
    default=True
)

registrationPage = s.Page(
    page="weps/registration.py",
    title="Registration",
    icon=":material/how_to_reg:"
)

attendancePage = s.Page(
    page= "weps/attendance.py",
    title="Attendance",
    icon=":material/scan:"
)

logs = s.Page(
    page="weps/logs.py",
    title="Logs",
    icon=":material/article:"
)

installer = s.Page(
    page="weps/install.py",
    title="dlib Install",
    icon=":material/check:"
)

nav = s.navigation(
    {
        "Project Info": [about, installer],
     "Application": [registrationPage, attendancePage, logs],
    }
)
nav.run()
