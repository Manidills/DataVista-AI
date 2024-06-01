from explorer.filecoin import file
from explorer.near import near_app
from explorer.weatherxm import weatherxm
import streamlit as st
import pandas as pd
import requests
from lit import wallet_con



def exp():
    option = st.selectbox(
   "Select Network",
   ("Near [Premium]", "Filecoin", "WeatherXM"),
   index=0,
   placeholder="Select contact method...",
)
    
    if option == 'Near [Premium]':

        if wallet_con() == True:
            near_app()
        else:
            st.info("Please connect Wallet for authentication")
    elif option == 'Filecoin':
        file()
    elif option == 'WeatherXM':
        weatherxm()