import streamlit as st
from streamlit_option_menu import option_menu  
from functionality import read_markdown_file

st.title("Electronics Projects")

st.header("Table of Contents")

md_path_01 = "pages/topic_projects/markdown/1_ArduinoProjectHandbook_p00.md"
ardProj0 = read_markdown_file(md_path_01)

display_page = ""

if st.button("1: Arduino Project Handbook Volume 1- Project 0"):
    display_page = ardProj0

st.markdown(display_page, unsafe_allow_html = True)

