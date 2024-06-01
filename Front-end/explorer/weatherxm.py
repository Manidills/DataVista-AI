import streamlit as st
import pandas as pd
import requests
import altair as alt
import numpy as np


def contract_all(url):

    url = url
    headers = {
        "accept": "application/json",'Connection':'close'
    }

    # Making the GET request
    response = requests.get(url, headers=headers)
    data = response.json()
    return data



def weatherxm():
    network_df = contract_all("https://api.weatherxm.com/api/v1/network/stats")

    st.markdown("#")
    st.markdown("#")
    col1, col2= st.columns(2)
    col1.metric("WXM Total Supplies ",contract_all('https://api.weatherxm.com/api/v1/network/stats/supply/total'))
    col2.metric("WXM Circulating Amount", contract_all('https://api.weatherxm.com/api/v1/network/stats/supply/circulating'))
    col1.metric(" Customers Total ",network_df['customers']['total'])
    col2.metric(" Customers With Wallets", network_df['customers']['with_wallet'])
   

    st.markdown("##")
    a,b = st.columns([2,2])
    with a:
        st.subheader("onboarded")
        st.write(network_df['weather_stations']['onboarded'])
    with b:
        st.subheader("claimed")
        st.write(network_df['weather_stations']['claimed'])

    data_days = pd.DataFrame(network_df['data_days'])
    data_days['ts'] = pd.to_datetime(data_days['ts'])
    st.markdown("##")
    st.altair_chart(
        alt.Chart(data_days).mark_circle().encode(
            y=alt.Y('value:N', scale=alt.Scale(reverse=True)),
            x="ts:T",  
        ).properties(
        width=800,
        height=300
    ),  use_container_width=True
    )

    area = st.text_input("Enter the area")
    if area :
        area = contract_all(f'https://api.weatherxm.com/api/v1/network/search?query={area}&exact=true')
        addresses = area.get("addresses", [])
        lat_lon_list = [{"lat": addr["center"]["lat"], "lon": addr["center"]["lon"]} for addr in addresses]
        df = pd.DataFrame(lat_lon_list)
        st.map(df)
    else:
        cells = contract_all(f'https://api.weatherxm.com/api/v1/cells')
        
        df_cells = pd.DataFrame([{'lat': item['center']['lat'], 'lon': item['center']['lon']} for item in cells])
        st.map(df_cells)

        st.markdown('##')
        st.write(pd.DataFrame(cells))

    st.markdown("##")

    area_index = st.text_input("Enter the index")

    if area_index:
        area_index = contract_all(f'https://api.weatherxm.com/api/v1/cells/{area_index}/devices')
        st.write(area_index)