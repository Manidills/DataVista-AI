import streamlit as st
import pandas as pd
import requests
import altair as alt
import numpy as np
import time


def contract_all(url):

    from requests.exceptions import ConnectionError

    # ...

    nb_tries = 10
    while True:
        nb_tries -= 1
        try:
            url = url
            headers = {
                "accept": "application/json",
                "authorization": "Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6ImtleS1iZXJ5eC0wMDEiLCJ0eXAiOiJKV1QifQ.eyJyb2xlcyI6W10sImlzcyI6IlpvbmRheCIsImF1ZCI6WyJiZXJ5eCJdLCJleHAiOjE3MjA5NzY0MDcsImp0aSI6Ik1hbmlrYW5kYW40MSxtYW5pQGJpdHNjcnVuY2guY29tIn0.dN9ygtiZ4WsLdsq3sSh_rDdWsV2bujKzj1qRCcfyhr5Delk7CjwYaGcyTtOZCRNcoDTV9ff3Aev_OutpDM4WsA"
            }

            # Making the GET request
            response = requests.get(url, headers=headers)
            data = response.json()
                    # Request url
            break
        except ConnectionError as err:
            if nb_tries == 0:
                raise err
            else:
                time.sleep(1)

    
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
    index_df = pd.read_csv('Front-end/explorer/cell_index.csv')
    st.data_editor(index_df,  num_rows="dynamic",use_container_width=True)
    df_normalized = pd.json_normalize(index_df['current_weather'])

    # Concatenate the original 'id' column with the normalized DataFrame
    result_df = pd.concat([index_df['cellIndex'], index_df['timezone'],df_normalized], axis=1)
    st.markdown("##")

    area_index = st.text_input("Enter the index")

    if area_index:
        area_index = contract_all(f'https://api.weatherxm.com/api/v1/cells/{area_index}/devices')
        st.write(area_index)
    else:
        st.data_editor(result_df,  num_rows="dynamic",use_container_width=True)