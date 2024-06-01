from explorer.filecoin import file
from explorer.near import near_app
from explorer.weatherxm import weatherxm
import streamlit as st
import pandas as pd
import requests



def exp():
    option = st.selectbox(
   "Select Network",
   ("Near", "Filecoin", "WeatherXM"),
   index=None,
   placeholder="Select contact method...",
)
    
    if option == 'Near':
        near_app()
    elif option == 'Filecoin':
        file()
    elif option == 'WeatherXM':
        weatherxm()