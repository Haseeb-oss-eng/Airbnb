import streamlit as st
import pandas as pd

def app():
    default_amenities = pd.read_csv("property_type.csv")
    df = pd.read_csv("transformed_data_geo.csv")
    amenities = ['Select a property type...'] + list(df['amenities'].dropna().unique())
    

    option = st.selectbox("Choose Amenity: ",amenities)
    result = df[df['amenities'].fillna("").str.contains(option, case=False)]

    st.dataframe(result)