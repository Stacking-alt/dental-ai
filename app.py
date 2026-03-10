import streamlit as st
import os
from dotenv import load_dotenv
from retell import Retell
import pandas as pd

# This finds the absolute path of your current folder
current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '.env')

# Load the .env file explicitly
load_dotenv(dotenv_path)

api_key = os.getenv("cal_live_b13d38df3fefbe5f1798604a270895ed")
agent_id = os.getenv("4965348")

# Debugging: This will help us see if the keys are loading
if not api_key:
    st.error(f"❌ API Key not found! Searching in: {dotenv_path}")
    st.stop() # Stops the app here so we can fix the path
else:
    client = Retell(api_key=api_key)
    st.success("✅ Connected to Retell AI")