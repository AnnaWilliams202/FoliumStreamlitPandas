import pandas as pd
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import st_folium


st.set_page_config(layout="wide")
st.title('Map of T-Intersection Vehicle Accidents with Clustering')
data = pd.read_csv('accidents.csv',sep = ';')
#print(data.head())

m = folium.Map(Location=[34, -86], zoom_start=4)
marker_cluster = MarkerCluster()

for i, row in data.iterrows():
    lat = row['LATITUDE']
    lon = row['LONGITUD']

    folium.Marker(
        location=[lat, lon],
        tooltip=row['MAN_COLLNAME']
     ).add_to(marker_cluster)

marker_cluster.add_to(m)
#m.save('map.html')
st_folium(m, width=1400)



