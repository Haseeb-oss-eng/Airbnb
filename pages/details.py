import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from folium import Popup

def app():
    data = pd.read_csv("transformed_data_geo.csv",encoding='utf-8')

    choose = st.selectbox("Choose Filter:",['Property Type','Price','Bed Type', 'Street'])

    if choose == 'Property Type':    
        property_type = ['Select a property type...'] + list(data['property_type'].dropna().unique())
        property_t = st.selectbox("Select the choice:",property_type)
        query = data[data['property_type']==property_t]

        if len(query)>0:
            for i in range(len(query)):
                if not query.empty:
                    record = query.iloc[i]  # Safely access the first row

                    st.markdown(f"<h4>Name: {record.get('name', 'N/A')}</h4>", unsafe_allow_html=True)
                    st.markdown(f"<p><b>{record.get('street', 'No address provided.')}</b></p>", unsafe_allow_html=True)
                    st.markdown(f"<p>{record.get('description', 'No description.')}</p>", unsafe_allow_html=True)

                    if pd.notna(record.get('picture_url')):
                        st.image(record['picture_url'], use_container_width=True)
                    else:
                        st.write("No image available.")
                else:
                    st.write("Select the option")
        else:
            st.write("Dataset is Empty!")
    elif(choose=="Price"):
        sorts = st.selectbox("Price Filter",["Lowest to Highest", "Highest to Lowest"])
        geo_l = data.sort_values(by='price_F')

        if sorts == "Lowest to Highest":
            for m in range(len(geo_l)):
                record = geo_l.iloc[m]  # Safely access the first row

                st.markdown(f"<h4>Name: {record.get('name', 'N/A')}</h4>", unsafe_allow_html=True)
                st.markdown(f"<h6><em>Price: ${record.get('price_F')}</em></h6>",unsafe_allow_html=True)
                st.markdown(f"<p><b>{record.get('street', 'No address provided.')}</b></p>", unsafe_allow_html=True)
                st.markdown(f"<p>{record.get('description', 'No description.')}</p>", unsafe_allow_html=True)

                if pd.notna(record.get('picture_url')):
                    st.image(record['picture_url'], use_container_width=True)
                else:
                    st.write("No image available.")
        elif sorts == "Highest to Lowest":
            geo_h = data.sort_values(by='price_F',ascending=False)
            for k in range(len(geo_h)):
                record = geo_h.iloc[k]  # Safely access the first row

                st.markdown(f"<h4>Name: {record.get('name', 'N/A')}</h4>", unsafe_allow_html=True)
                st.markdown(f"<h6><em>Price: ${record.get('price_F','0')}</em></h6>",unsafe_allow_html=True)
                st.markdown(f"<p><b>{record.get('street', 'No address provided.')}</b></p>", unsafe_allow_html=True)
                st.markdown(f"<p>{record.get('description', 'No description.')}</p>", unsafe_allow_html=True)

                if pd.notna(record.get('picture_url')):
                    st.image(record['picture_url'], use_container_width=True)
                else:
                    st.write("No image available.")

    elif choose=="Bed Type":
        property_type = ['Select a property type...'] + list(data['bed_type'].dropna().unique())
        property_t = st.selectbox("Select the choice:",property_type)
        query = data[data['bed_type']==property_t]

        if len(query)>0:
            for i in range(len(query)):
                if not query.empty:
                    record = query.iloc[i]  # Safely access the first row

                    st.markdown(f"<h4>Name: {record.get('name', 'N/A')}</h4>", unsafe_allow_html=True)
                    st.markdown(f"<p><b>{record.get('street', 'No address provided.')}</b></p>", unsafe_allow_html=True)
                    st.markdown(f"<p>{record.get('description', 'No description.')}</p>", unsafe_allow_html=True)

                    if pd.notna(record.get('picture_url')):
                        st.image(record['picture_url'], use_container_width=True)
                    else:
                        st.write("No image available.")
                else:
                    st.write("Select the option")
        else:
            st.write("Dataset is Empty!")
    
    elif choose == "Street":        
        property_type = ['Select a property type...'] + list(data['street'].dropna().unique())
        property_t = st.selectbox("Select the choice:", property_type)
        query = data[data['street'] == property_t]

        if len(query)>0:
            for i in range(len(query)):
                record = query.iloc[i]

                pop = f"<h5><b>State: {record.get('state', 'N/A')}</b></h5><br> <p><b>{record.get('street', 'No address provided.')}</b></p> <p><i>Price: ${record.get('price_F', 'No amount')}</i></p>"
                popups = Popup(pop,max_width=250)
                m = folium.Map(location=[record.get('latitude'), record.get('longitude')],zoom_start=10)
                folium.Marker(
                    location=[record.get('latitude'), record.get('longitude')],
                    popup=popups,
                    icon=folium.Icon(color="blue", icon="home")
                ).add_to(m)
                st_folium(m, width=700, height=500)

                if pd.notna(record.get('picture_url')):
                    st.image(record['picture_url'], use_container_width=True)
                else:
                    st.write("No image available.")
        else:
            st.write("There is no data available for the selected property type.")