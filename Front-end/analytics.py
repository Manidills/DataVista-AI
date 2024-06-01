import streamlit as st
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import altair as alt
import numpy as np
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import requests
import tempfile
import base64


def try_convert_to_datetime(df, column):
    try:
        df[column] = pd.to_datetime(df[column])
        return True
    except ValueError:
        return False

def categorize_columns(df):
    datetime_cols = []
    numeric_cols = []
    string_cols = []

    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            datetime_cols.append(col)
        elif pd.api.types.is_numeric_dtype(df[col]):
            numeric_cols.append(col)
        elif df[col].dtype == object and try_convert_to_datetime(df, col):
            datetime_cols.append(col)
        else:
            string_cols.append(col)
    
    return datetime_cols, numeric_cols, string_cols

def plot_permutations(df, datetime_cols, numeric_cols, string_cols):
    permutations = list(itertools.product(datetime_cols, numeric_cols + string_cols))
    for (dt_col, val_col) in permutations:
        plt.figure(figsize=(10, 5))
        plt.plot(df[dt_col], df[val_col], marker='o')
        plt.title(f'{val_col} over {dt_col}')
        plt.xlabel(dt_col)
        plt.ylabel(val_col)
        st.pyplot(plt)
        plt.close()

def estuary(file):
    file = open(file, "rb")
    response = requests.post(
        "https://upload.estuary.tech/content/add",
        headers={"Authorization": f"Bearer {'ESTb4e2b39a-6435-4a5a-9a84-6f34df047ad3ARY'}"},
        files={"data": file}
    )

    return response


def lighthouse(file):
    file = open(file, "rb")
    response = requests.post(
        "https://node.lighthouse.storage/api/v0/add",
        headers={"Authorization": f"Bearer {'97cef50c.2579ee5d584d4dc69855caa30d3b582c'}"},
        files={"file": file}
    )

    return response

def moralis(file):
    api_key = "7hstobdqT97qzSbNkW6Spq227cMCBXEPsKBAM7yk70Wqhiygi3uHD7snLqupcL46"


    file = open(file, "rb")

    try:
        content = base64.b64encode(file).decode('utf-8')
    except:
        content = base64.b64encode(file.read()).decode('utf-8')

    response = requests.post(
        "https://deep-index.moralis.io/api/v2/ipfs/uploadFolder",
        headers={"X-API-Key": api_key},
        json=[{"path": f"dummy", "content": content}],
    )
    path = response.json()[0]['path']
    return path.split("/ipfs/")[-1]


def data(df):
    
        
        # st.write("Dataframe Preview:")
        # st.dataframe(df.head())

        
        datetime_cols, numeric_cols, string_cols = categorize_columns(df)
        
        # st.write("Datetime columns:", datetime_cols)
        # st.write("Numeric columns:", numeric_cols)
        # st.write("String columns:", string_cols)
        
        # if datetime_cols:
        #     plot_permutations(df, datetime_cols, numeric_cols, string_cols)
        # else:
        #     st.write("No datetime columns found to plot against.")

        st.markdown("##")
        st.write("""
            ### Editable DataFrame Preview ###
            """)
        st.markdown("##")
        st.data_editor(df,  num_rows="dynamic",use_container_width=True)

        st.markdown("##")
        if datetime_cols != None:
            if len(numeric_cols)  % 2 == 0:
                a, b = st.columns([2, 2])
                for i, column in enumerate(numeric_cols):
                        if i % 2 == 0:
                            pos = a
                        else:
                            pos = b

                        with pos:
                            st.altair_chart(
                                alt.Chart(df).mark_bar(color='red').encode(
                                    x=alt.X(datetime_cols[0], title='Date'),
                                    y=alt.Y(column, title=column.replace('_', ' ').title())
                                ).properties(
                                    width=800,
                                    height=300,
                                ), use_container_width=True
                            )
            else:
                for column in numeric_cols:
                    st.altair_chart(
                    alt.Chart(df).mark_line(color='red').encode(
                        x=alt.X(datetime_cols[0], title='Date'),
                        y=alt.Y(column, title=column.replace('_', ' ').title())
                    ).properties(
                        width=800,
                        height=300,
                        title=f"{column.replace('_', ' ').title()} Over Time"
                    ),  use_container_width=True)


        st.markdown("##")
        with st.expander('Check Report'):
            pr = ProfileReport(df, explorative=True)
            st_profile_report(pr)


def analytics():

    st.title("Automatic Analyzer")

   
    with st.form("my_form"):
        uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xlsx'])

        genre = st.radio(
            "Push the file to IPFS via",
            ("LightHouse",  'Moralis/Pinata','Web3_Storage', 'NFTPORT', 'Estuary'),horizontal=True)
        
        ask_pdf = st.form_submit_button("submit")

        if ask_pdf:
            if uploaded_file:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith('.xlsx'):
                    df = pd.read_excel(uploaded_file)
            
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                temp.write(uploaded_file.getvalue())
        
            if genre == 'LightHouse':

                    store_data = lighthouse(temp.name)
                    url = store_data.json()['Hash']
                    new_url = f'https://gateway.lighthouse.storage/ipfs/{url}'
                    st.success(f'Can download/view data from {new_url}')
                    data(df)
            elif genre == 'Moralis/Pinata':
                store_date = moralis(temp.name)
                ipfs_gateway = 'https://ipfs.moralis.io'
                # Concatenate the IPFS gateway URL with the CID
                new_url = f"https://ipfs.moralis.io/ipfs/{store_date}"
                st.success(f'Can download/view data from {new_url}')
                data(df)
            elif genre == 'Estuary':
                store_data = estuary(temp.name)
                url = store_data.json()['cid']
                new_url = f'https://api.estuary.tech/gw/ipfs/{url}'
                st.success(f'Can download/view data from {new_url}')
                data(df)
            else:
                st.info("404")






                