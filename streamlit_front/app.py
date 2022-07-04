import requests
import streamlit as st

st.write("Hello")
res = requests.get("http://backend:8080/")
out = res.json()

st.write(out.get("Hello"))
