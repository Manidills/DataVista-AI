from io import StringIO
import sqlite3
import requests
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import altair as alt
import math


def connect_db():

    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = """SELECT cid from lighthouse"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records





def cube3claims():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[0][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['date'] = pd.to_datetime(df['date'])
    return df

def cube3c2():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[1][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['date'] = pd.to_datetime(df['date'])
    return df

def cube3c3():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[6][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['dt'] = pd.to_datetime(df['dt'])
    return df

def cube3c4():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[7][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['date'] = pd.to_datetime(df['date'])
    return df

def cube3c5():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[8][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['date'] = pd.to_datetime(df['date'])
    return df

def framesc1():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[2][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['dt'] = pd.to_datetime(df['dt'])
    return df

def framesc2():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[3][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['dt'] = pd.to_datetime(df['dt'])
    return df

def framesc3():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[4][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['dt'] = pd.to_datetime(df['dt'])
    return df

def framesc4():
    records = connect_db()
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records[10][0]}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['dt'] = pd.to_datetime(df['dt'])
    return df


def dash():

    option = st.selectbox(
   "How would you like to be contacted?",
   ("Layer3_Cubes", "Frames"),
   index=None,
   placeholder="Select contact method...",
)
    
    if option == "Layer3_Cubes":
        claims = cube3claims()
        
        
        st.markdown("##")
        st.write("""
            ### Total Claims ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(claims).mark_line().encode(
                y='claims:N',
                x="date:T",  
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )

        st.markdown("##")
        st.write("""
            ### Total Claims ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(cube3c2()).mark_line(color='green').encode(
                y='unique_wallets:N',
                x="date:T",  
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )


        st.markdown("##")
        a,b = st.columns([2,2])
        with a:
        
            st.markdown("##")
            st.write("""
                ### Chain Claims ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(cube3c3()).mark_arc().encode(
                    theta='claims',
                    color="chain",    
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )
        
        with b:
            st.markdown("##")
            st.write("""
                ### Chain Claims Share  ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(cube3c3()).mark_arc().encode(
                   theta='chain_share',
                   color="chain", 
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
        
            )

        st.markdown("##")
        st.write("""
            ### Chain Wise Claims ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(cube3c4()).mark_line().encode(
                y='claims:N',
                x="date:T",    
                color='chain',
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )


        st.markdown("##")
        a,b = st.columns([2,2])
        with a:
        
            st.markdown("##")
            st.write("""
                ### Cube Grouped Wallets ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(cube3c5()).mark_arc().encode(
                    theta='Wallets:N',
                    color="cubes_claimed_group",    
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )
        
        with b:
            st.markdown("##")
            st.write("""
                ### Cube Grouped Share  ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(cube3c5()).mark_arc().encode(
                   theta='share:N',
                   color="cubes_claimed_group", 
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
        
            )
        st.write(cube3c4())
    if option == "Frames":


        st.markdown("##")
        st.write("""
            ### Num Reach ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(framesc1()).mark_line(color='red').encode(
                y='num_reach:N',
                x="dt:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )

        st.markdown("##")
        a,b = st.columns([2,2])
        with a:
            st.markdown("##")
            st.write("""
                ### Num Casts ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(framesc1()).mark_area(color='pink').encode(
                    y='num_casts:N',
                    x="dt:T",    
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )

            st.markdown("##")
            st.write("""
                ### Num Recasts ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(framesc1()).mark_area(color='white').encode(
                    y='num_recasts:N',
                    x="dt:T",    
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )
        with b:
            st.markdown("##")
            st.write("""
                ### Num Likes ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(framesc1()).mark_line(color='green').encode(
                    y='num_likes:N',
                    x="dt:T",    
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )

            st.markdown("##")
            st.write("""
                ### Num Replies ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(framesc1()).mark_line(color='yellow').encode(
                    y='num_replies:N',
                    x="dt:T",    
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )
        st.markdown("##")
        st.write("""
            ### Num Engagement ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(framesc1()).mark_bar(color='blue').encode(
                y='num_engagement:N',
                x="dt:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )

        st.markdown("##")
        st.write(framesc1())

        st.markdown("##")
        a,b = st.columns([2,2])
        with a:
        
            st.markdown("##")
            st.write("""
                ### Channel Fids ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(framesc2()).mark_arc().encode(
                    theta='num_fids:N',
                    color="channel",    
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
            )
        
        with b:
            st.markdown("##")
            st.write("""
                ### Channel Casts  ###
                """)
            st.markdown("##")
            st.altair_chart(
                alt.Chart(framesc2()).mark_arc().encode(
                   theta='num_casts:N',
                   color="channel", 
                ).properties(
                width=800,
                height=300
            ),  use_container_width=True
        
            )
        
        st.markdown("##")
        st.write("""
            ### Base Transactions ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(framesc4()).mark_line().encode(
                y='base_transactions:N',
                x="date:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )

        st.markdown("##")
        st.write("""
            ### Zora Transactions ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(framesc4()).mark_line(color='white').encode(
                y='zora_transactions:N',
                x="date:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )

        st.markdown("##")
        st.write("""
            ### Optimisim Transactions ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(framesc4()).mark_line(color='blue').encode(
                y='optimism_transactions:N',
                x="date:T",    
            ).properties(
            width=800,
            height=300
        ),  use_container_width=True
        )

        st.write(framesc4())








