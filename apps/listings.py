import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import folium

def app():

    st.title("Airbnb Listings Map")

    # Load Airbnb data with latitude, longitude, name, and price
    data = pd.read_csv("data/listings_clean.csv", usecols=["latitude", "longitude", "name", "price"])

    # Create a Leafmap with OpenStreetMap tiles
    m = leafmap.Map(tiles="OpenStreetMap")

    # Add Airbnb listings as labeled markers
    for i, row in data.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['name']} ({row['price']})",
            icon=None,
            tooltip=None,
        ).add_to(m)

    # Display the Leafmap in Streamlit
    m.to_streamlit(height=700)
