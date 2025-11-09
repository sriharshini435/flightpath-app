
import matplotlib.pyplot as plt
import cartopy.crs as c
import cartopy.feature as cf
import numpy as np
import streamlit as st
st.title('Flight app ')
st.subheader('this app displays the flight path between any two cities ')
cities = {
    'New York': [40.7128, -74.0059],
    'London': [51.5074, -0.1278],
    'Tokyo': [35.6895,139.6917],
    'Sydney': [-33.8688,151.2093],
    'Cape Town': [-33.9249,18.4241],
    'Rio de Janeiro': [-22.9068,-43.1729],
    'Paris' : [48.8566,2.3522 ],
    'Moscow' : [55.7558,37.6173],
    'Mumbai' : [ 19.0760,72.8777]
}
ci=cities.keys()
source=st.selectbox('choose the source city',ci)
d=st.selectbox('choose the destinstion city',ci)
def map_plot(extent):
    fig = plt.figure(figsize=(20,15))
    ax = plt.axes(projection = c.PlateCarree())
    ax.set_extent(extent, crs = c.PlateCarree())
    ax.add_feature(cf.OCEAN)
    ax.add_feature(cf.LAND)
    ax.add_feature(cf.COASTLINE)
    ax.add_feature(cf.RIVERS)
    return ax,fig

def city_plot(lon_city,lat_city,ax,city_name):
    ax.plot(lon_city,lat_city,marker = 'o',color = 'red', transform = c.PlateCarree())
    ax.text(lon_city+2,lat_city-3,city_name, color = 'black', transform = c.PlateCarree())

if st.button('flight path'):
    extent = [-180, 180, -90, 90]
    ax,fig= map_plot(extent)

    for city, (lat, lon) in cities.items():
        city_plot(lon, lat, ax, city)
    city1 = source
    city2 = d
    lat_a, lon_a = cities[city1]
    lat_b, lon_b = cities[city2]
    ax.plot([lon_a, lon_b], [lat_a, lat_b], color="green", transform=c.Geodetic())

    st.pyplot(fig)










