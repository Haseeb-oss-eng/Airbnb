import streamlit as st
from pages import Info  # Import the Info module from pages folder
from pages import details

st.sidebar.title("Airbnb App")
selection = st.sidebar.radio("Go to", ["Home", "Details", "Display"])

if selection == "Home":
    st.title("Airbnb Listing")
    st.write("Welcome to the Airbnb Dashboard!")
elif selection == "Details":
    Info.app()  # Call the app() function from Info.py
elif selection == "Display":
    details.app()