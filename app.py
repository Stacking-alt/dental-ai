import streamlit as st
import os
from dotenv import load_dotenv
from retell import Retell
import pandas as pd

# 1. Load local .env (for your computer)
load_dotenv()

# 2. Get keys from Streamlit Secrets (for Cloud) or .env (for Local)
# NOTE: We use the names of the variables, not the keys themselves here
# CORRECT WAY: Use the Variable Names, not the actual long keys
api_key = st.secrets.get("RETELL_API_KEY") or os.getenv("RETELL_API_KEY")
agent_id = st.secrets.get("AGENT_ID") or os.getenv("AGENT_ID")

if not api_key:
    st.error("API Key not found! Please check your Streamlit Secrets or .env file.")
    st.stop()

client = Retell(api_key=api_key)
st.success(" Connected to Smile 4 U AI")

# --- Dashboard UI ---
st.title("🦷 Smile 4 U AI Receptionist")

patient_number = st.text_input("Enter Patient Number (e.g., +91...)")
if st.button("Start AI Call"):
    try:
        call = client.call.create_phone_call(
            from_number="+1234567890", # Replace with your Retell number
            to_number=patient_number,
            agent_id=agent_id
        )
        st.success(f"Call started! ID: {call.call_id}")
    except Exception as e:
        st.error(f"Call failed: {e}")