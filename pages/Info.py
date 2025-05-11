import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def app():
    st.title("Boston Listings")
    list_data = pd.read_csv("transformed_data_geo.csv").sort_values(by='price_F',ascending=False)
    st.dataframe(list_data,use_container_width=True)

    m = folium.Map(location=[42.347934, -71.097580], zoom_start=13)
    c = 0
    # Loop through dataframe and add markers
    for _, row in list_data.iterrows():
        if c<4:
            lat = row['latitude']
            lon = row['longitude']
            name = row.get('street', 'Not Area')
            price = row.get('price', 'N/A')

            popup_text = f"{name}<br>Price: {price}"
            folium.Marker(
                location=[lat, lon],
                popup=popup_text,
                icon=folium.Icon(color="blue", icon="home")
            ).add_to(m)
            c+=1
        else:
            break
    # Show the map in Streamlit
    st.title("Airbnb Listings with Markers")
    st_folium(m, width=700, height=500)