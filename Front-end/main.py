import base64
import io
import os
import PyPDF2
import tempfile
from PIL import Image
from db import dash
from explorer.exp import exp
from explorer.near import near_app
import streamlit as st
import requests
from wallet_connect import wallet_connect
from analytics import analytics
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import io


st.set_page_config(
    page_title="DataVista-AI",
    page_icon="❄️️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates scripts for data clean rooms!"
    }
)


st.sidebar.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDFjb2UzaWFwMnZqZWE1b2N3Yjc5OTltYzdxM2h5YXY2MWd6MXBxbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/UAragLbg9oKRfZLThq/giphy.webp")
action = st.sidebar.radio("What action would you like to take?", ("About","Dashboards","Analytics", "Explorer"))

def wallet_con():
    with st.sidebar:
        st.markdown('##')
        wallet =  wallet_connect(
            label="login", 
            key="login", 
            message="Login", 
            auth_token_contract_address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            chain_name="ethereum", 
            contract_type="ERC20",
            num_tokens="0"
            )
        return wallet
    


if action == "Analytics":
    analytics()
elif action == "Explorer":
    exp()
elif action == "Dashboards":
    dash()
elif action == "About":
    

    # Set the title of the web app
    st.title("Welcome to our Decentralytics")

    st.write("""
    The project aims to address a significant challenge faced by analytics companies: managing and storing massive amounts of data in a table, and providing a common platform for users to access analytical insights for their data freely. 

    To solve this problem, we have developed a decentralized solution leveraging Filecoin and IPFS technologies. Our project establishes a specific pipeline that collects data in batches and stores it on IPFS. When a user requests a table using a CID (Content Identifier), the data is retrieved directly from IPFS, eliminating the need for centralized data storage.

    """)


    # Dashboard Section
    st.header("Dashboards")
    st.write("""
    Our dashboard section is designed to collect trending Web3 protocols data in streaming batches and upload it to Filecoin/IPFS. When a user enters this section, it triggers a specific CID that is encrypted with the help of the LIT protocol. The data is then decrypted and made accessible to users.

    Our dbt DAGs (Data Build Tool Directed Acyclic Graphs) work continuously to collect new data in batches, ensuring that the most current information is always available.
    """)

    # Analytics Section
    st.header("Analytics")
    st.write("""
    Our AI-based model allows users to upload their data and performs an in-depth analysis of each column, summarizing the findings. These data and findings are then made available via an IPFS URL. This enables anyone to obtain analytics insights without needing any coding knowledge.
    """)

    # Explorer Section
    st.header("Explorer")
    st.write("""
    Our Explorer section actively collects data from different blockchain networks to identify anomalies and perform statistical analysis. Users can explore all activities that have occurred in these networks using various filters.

    We have a pipeline that gathers data from open networks and stores it on Filecoin/IPFS in a streaming manner. This ensures that the data is always up-to-date and can be utilized effectively.
    """)

    # Footer
    st.markdown("##")
    a,b = st.columns([2,2])
    with a:
        st.success(f"Source data from {'https://docs.lighthouse.storage'}")
        st.success(f"Source data from {'https://web3.storage/docs'}")
        st.success(f"Source data from {'https://docs.estuary.tech'}")
        st.success(f"Source data from {'https://docs.nftport.xyz/reference/upload-file-to-ipfs'}")
    with b:
        st.success(f"Source data from {'https://moralis.io/how-to-upload-files-to-ipfs-full-guide'}")
        st.success(f"Source data from {'https://github.com/LIT-Protocol/js-sdk'}")
        st.success(f"Source data from {'https://docs.zondax.ch/openapi#auth'}")
        st.success(f"Source data from {'https://api.weatherxm.com/api/v1/docs/#/'}")

