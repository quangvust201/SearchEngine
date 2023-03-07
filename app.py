import streamlit as st
import requests


st.set_page_config(page_title="Google Search Clone", page_icon=":mag:")

st.title("Google Search Clone")

query = st.text_input("Enter your search query", "")

if st.button("Search"):
    with st.spinner(f"Searching for '{query}'..."):
        data = requests.get(f"http://127.0.0.1:8000/search?query={query}").json()
        st.markdown(f"## Results for {query}")
        for x in data:
            st.write(x)
        
