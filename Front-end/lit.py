import streamlit as st
import requests
from wallet_connect import wallet_connect



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