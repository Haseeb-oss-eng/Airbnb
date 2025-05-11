import streamlit as st
from pages import Info, details, amenities

st.sidebar.title("Airbnb App")
option = st.sidebar.radio("Tab",["About Us", "Listing Properties", "Customized Information", "Amenities"])


if option == "About Us":
    st.title("Air Bed and Breakfast")
    st.markdown(
        """
        <p style='text-align: justify;'>
        Airbnb, an abbreviation of its original name, "Air Bed and Breakfast", is an American company operating an online marketplace for short-and-long-term homestays and experiences in various countries and regions. It acts as a broker and charges a commission from each booking. Airbnb was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. It is the best-known company for short-term housing rentals.
        </p>
        """,
        unsafe_allow_html=True
    )
elif option == "Listing Properties":
    Info.app()
elif option == "Customized Information":
    details.app()
elif option == "Amenities":
    amenities.app()