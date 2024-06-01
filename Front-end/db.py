from io import StringIO
import sqlite3
import requests
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import altair as alt
import math


def LIT_call(encrypted_cid):

    response = requests.get(f'https://datavista-ai.onrender.com/api/user/decryptFile/{encrypted_cid}', headers={'Connection':'close'})
    res_json = response.json()
    return res_json['data']['cid']

def connect_db():

    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)

    sqlite_select_query = """SELECT cid from lighthouse"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records
    





def cube3claims():
    records = LIT_call('76892e207d068ca8887188620bf824781934c60910b8b79af7a93b5a316460cc')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['date'] = pd.to_datetime(df['date'])
    return df

def cube3c2():
    records = LIT_call('799a24cd0985ebf8ec27aee3e4560916b72bb7fc4388eeb11e33059148467ffc')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['date'] = pd.to_datetime(df['date'])
    return df

def cube3c3():
    records = LIT_call('527c14b284f0360087d22fb8a5c7d303371a27842f249f751bc541dc0df33545')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['dt'] = pd.to_datetime(df['dt'])
    return df

def cube3c4():
    records = LIT_call('7a0e4bc28ba8de96e284b2e0e728529198c8e1ebcbc3da4d9ade1067195065ef')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['date'] = pd.to_datetime(df['date'])
    return df

def cube3c5():
    records = LIT_call('455e7f5f40cbfb885e1aab32ebf9c560185ad59c81e02ed6cf7af934f23d6c8c')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['date'] = pd.to_datetime(df['date'])
    return df

def framesc1():
    records = LIT_call('c470efbd4afe96bf6bc5152ad68cba75730f09e18f8511bf36008d9b9cff4a81')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    df['dt'] = pd.to_datetime(df['dt'])
    return df

def framesc2():
    records = LIT_call('09f12d7391b2937115be365c79da8b638fc83bd85068df25c3f94f09eb2c7cbe')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['dt'] = pd.to_datetime(df['dt'])
    return df

def framesc3():
    records = LIT_call('3ba6db5c9fb7890108887ce669651e1e37babc96391cc3eb7af4c4b7056b29c1')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)
    #df['dt'] = pd.to_datetime(df['dt'])
    return df

def framesc4():
    records = LIT_call('e5551a497288b8aeeb38777a516bc59a36f8c560694bc84c70d54429e27845f2')
    response = requests.get(f'https://gateway.lighthouse.storage/ipfs/{records}', headers={'Connection':'close'})
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
            ### Unique Wallets ###
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
                alt.Chart(framesc1()).mark_area(color='black').encode(
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
            alt.Chart(framesc4()).mark_line(color='green').encode(
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








