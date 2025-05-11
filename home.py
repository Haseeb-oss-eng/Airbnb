import streamlit as st
from pages import Info, details

st.sidebar.title("Airbnb App")
option = st.sidebar.radio("Tab",["About Us", "Listing Properties", "Customized Information"])


if option == "About Us":
    st.title("Airbnb")

elif option == "Listing Properties":
    Info.app()
elif option == "Customized Information":
    details.app()