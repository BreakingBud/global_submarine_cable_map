import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import folium_static

# Load GeoJSON files
cables_path = 'cables.geojson'
landing_points_path = 'landing-points.geojson'

cables_gdf = gpd.read_file(cables_path)
landing_points_gdf = gpd.read_file(landing_points_path)

# Initialize Folium map
m = folium.Map(location=[0, 0], zoom_start=2, tiles='cartodbpositron')

# Add cables to the map
for _, row in cables_gdf.iterrows():
    folium.GeoJson(row.geometry).add_to(m)

# Add landing points to the map
for _, row in landing_points_gdf.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=row['name'],
        icon=folium.Icon(color='blue', icon='point')
    ).add_to(m)

# Display the map in Streamlit
st.title('Global Cables and Landing Points Map')
folium_static(m)
