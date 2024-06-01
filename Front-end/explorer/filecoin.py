import streamlit as st
import pandas as pd
import requests
import altair as alt
import numpy as np



def contract_all(url):

    url = url
    headers = {
        "accept": "application/json",
        "authorization": "Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6ImtleS1iZXJ5eC0wMDEiLCJ0eXAiOiJKV1QifQ.eyJyb2xlcyI6W10sImlzcyI6IlpvbmRheCIsImF1ZCI6WyJiZXJ5eCJdLCJleHAiOjE3MjA5NzY0MDcsImp0aSI6Ik1hbmlrYW5kYW40MSxtYW5pQGJpdHNjcnVuY2guY29tIn0.dN9ygtiZ4WsLdsq3sSh_rDdWsV2bujKzj1qRCcfyhr5Delk7CjwYaGcyTtOZCRNcoDTV9ff3Aev_OutpDM4WsA"
    }

    # Making the GET request
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def file():
    st.title("Filecoin Network Explorer")

   
    with st.form("my_form"):
        address = st.text_input("Enter the Address")

        contract_address = st.text_input("Enter the contract_address")

        FIL_address = st.text_input("Enter the FIL")

        genre = st.radio(
            "Select Action",
            ('Account/Token'),horizontal=True)
        
        ask_pdf = st.form_submit_button("submit")

    if ask_pdf:
        if genre == 'Account/Token':
            st.subheader(" Account ERC20 transfer ")
            st.markdown("##")
            list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/transactions/erc20/address/{address}/transfers")
            st.write(pd.DataFrame(list_erc['transfers']))

            st.subheader(" Account ERC20  transactions in contract")
            st.markdown("##")
            list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/transactions/erc20/contract/{contract_address}/address/{address}/transfers")
            st.write(pd.DataFrame(list_erc['transfers']))

            st.subheader(" Gas used in txs ")
            st.markdown("##")
            list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/stats/gas-used/{FIL_address}/monthly?sort_by=bucket:desc")
            list_erc_df = pd.DataFrame(list_erc['results'])
            list_erc_df['bucket'] = pd.to_datetime(list_erc_df['bucket'])
            list_erc_df['gas_used'] = list_erc_df['gas_used'].astype(np.int64)

            st.markdown("##")
            st.altair_chart(
                alt.Chart(list_erc_df).mark_line().encode(
                    y='gas_used:N',
                    x="bucket:T",  
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )

            st.subheader(" Cumulative Gas used in txs ")
            st.markdown("##")
            list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/stats/gas-used/{FIL_address}/monthly/cumulative?sort_by=bucket:desc")
            list_erc_df = pd.DataFrame(list_erc['results'])
            list_erc_df['bucket'] = pd.to_datetime(list_erc_df['bucket'])
            list_erc_df['gas_used'] = list_erc_df['gas_used'].astype(np.int64)

            st.markdown("##")
            st.altair_chart(
                alt.Chart(list_erc_df).mark_line().encode(
                    y='gas_used:N',
                    x="bucket:T",  
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )

            st.markdown("##")
            a,b = st.columns([2,2])
            with a:
                st.subheader(" Account value exchanged ")
                st.markdown("##")
                list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/stats/value-exchanged/{FIL_address}/latest?data_points=10")
                st.write(pd.DataFrame(list_erc['results']))
            with b:
                st.subheader(" Exchanged cumulative ")
                st.markdown("##")
                list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/stats/value-exchanged/{FIL_address}/latest/cumulative")
                st.write(pd.DataFrame(list_erc['results']))

            st.markdown("##")


           
    else:
        st.subheader(" List of ERC20 contracts ")
        st.markdown("##")
        list_erc = contract_all("https://api.zondax.ch/fil/data/v3/mainnet/erc20/contracts?sort=holders&order=desc")
        st.write(pd.DataFrame(list_erc))

        st.markdown("##")

        st.subheader(" List of richest address ")
        st.markdown("##")
        rich_list = contract_all("https://api.zondax.ch/fil/data/v3/mainnet/stats/rich-list/10?sort_by=bucket:asc")
        st.write(pd.DataFrame(rich_list['results']))

        st.subheader(" Created contracts ")
        st.markdown("##")
        list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/stats/contract/global/create/monthly?sort_by=bucket:asc")
        list_erc_df = pd.DataFrame(list_erc['results'])
        list_erc_df['bucket'] = pd.to_datetime(list_erc_df['bucket'])

        st.markdown("##")
        st.altair_chart(
            alt.Chart(list_erc_df).mark_line().encode(
                y='count:N',
                x="bucket:T",  
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )

        st.subheader(" Created contracts Cumulative ")
        st.markdown("##")
        list_erc = contract_all(f"https://api.zondax.ch/fil/data/v3/mainnet/stats/contract/global/create/monthly/cumulative?sort_by=bucket:desc")
        list_erc_df = pd.DataFrame(list_erc['results'])
        list_erc_df['bucket'] = pd.to_datetime(list_erc_df['bucket'])

        st.markdown("##")
        st.altair_chart(
            alt.Chart(list_erc_df).mark_bar(color='red').encode(
                y='count:N',
                x="bucket:T",  
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )


        st.markdown("##")
        a,b = st.columns([2,2])
        with a:
            st.subheader(" Top contracts  ")
            st.markdown("##")
            rich_list = contract_all("https://api.zondax.ch/fil/data/v3/mainnet/stats/contract/top/unique-users?limit=10")
            st.write(pd.DataFrame(rich_list['results']))
        with b:
            st.subheader(" Top accounts by GAS   ")
            st.markdown("##")
            rich_list = contract_all("https://api.zondax.ch/fil/data/v3/mainnet/stats/gas-used/top/accounts?limit=10")
            st.write(pd.DataFrame(rich_list['results']))

        



