import streamlit as st
import pandas as pd
import numpy as np

st.title("Final Project")

expense_option = st.selectbox(
    "종류 선택",
    ("식비", "교통비", "기타"))

