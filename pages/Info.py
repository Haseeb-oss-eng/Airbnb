import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def app():
    st.title("Boston Listings")
    list_data = pd.read_csv("transformed_data_geo.csv").sort_values(by='price_F',ascending=False)
    st.dataframe(list_data,use_container_width=True)

    m = folium.Map(location=[42.347934, -71.097580], zoom_start=13)
    folium.Marker([42.347934, -71.097580], popup="Boston Marker").add_to(m)

    # Render it
    st_folium(m, width=700, height=500)