import streamlit as st
from streamlit_option_menu import option_menu  
from functionality import read_markdown_file

st.title("Software Development Projects")

st.header("Table of Contents")

mdpath01 = "pages/topic_projects/markdown/01_swdBookProj01.md"
oreillyproj1 = read_markdown_file(mdpath01)

displaypage = ""

if st.button("1: O'Reilly Book Ch 2 - The Bank Statements Analyzer"):
    displaypage = oreillyproj1

st.markdown(displaypage, unsafe_allow_html = True)

if st.button("Close Project"):
    display_page = ""