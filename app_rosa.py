import streamlit as st
from streamlit_folium import folium_static
import folium

def main():
    text="""
    # Aplicación de Machine Learning semiautomática (hands on)
    ## Esta aplicación ayuda  hacer un análisis de datos rápido

    > 
    """
    st.markdown(text)

    # center on UFA-ESPE
    m = folium.Map(location=[-0.3134717, -78.4448139], zoom_start=16)

    # add marker for UFA-ESPE
    tooltip = "UFA-ESPE"

    # i can use fot awesome icons in the icon 
    folium.Marker(
        [-0.3134717, -78.4448139], 
        popup='<b>UFA</b>-ESPE', 
        tooltip=tooltip, 
        icon=folium.Icon(prefix='fa',icon='fa-exclamation-triangle',color='red') 
    ).add_to(m)

    # Circle marker
    folium.CircleMarker(
        location=[-0.3134717, -78.4448139],
        radius=60,
        popup="Circulo",
        color="#428bca",
        fill=True,
        fillColor="#428bca"
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)

if __name__ == '__main__':
    main()