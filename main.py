import streamlit as st
import pandas as pd
from components.portfolio import render_portfolio_section
from components.lots import render_lots_section
from utils.data_manager import initialize_data

st.set_page_config(
    page_title="Stock Portfolio Manager",
    page_icon="📈",
    layout="wide"
)

# Initialize session state
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'portfolio'

# Initialize data
initialize_data()

# App title and navigation
st.title("📈 Stock Portfolio Manager")

# Navigation
col1, col2 = st.columns([1, 5])
with col1:
    view = st.radio(
        "Navigation",
        ["Portfolio", "Lots Management"],
        key="nav"
    )
    st.session_state.current_view = view.lower()

# Render appropriate view
if st.session_state.current_view == 'portfolio':
    render_portfolio_section()
else:
    render_lots_section()

# Footer
st.markdown("---")
st.markdown("### 📊 Stock Portfolio Manager - Track your investments efficiently")
