import streamlit as st
from streamlit_option_menu import option_menu  
from functionality import read_markdown_file

st.title("Electronics Projects")

st.header("Table of Contents")

md_path_01 = "pages/topic_projects/markdown/1_ArduinoProjectHandbook_p00.md"
ardProj0 = read_markdown_file(md_path_01)

md_path_02 = "pages/topic_projects/markdown/2_ArduinoProjectHandbook_p01.md"
ardProj1 = read_markdown_file(md_path_02)

md_path_03 = "pages/topic_projects/markdown/3_ArduinoProjectHandbook_p02.md"
ardProj2 = read_markdown_file(md_path_03)

display_page = ""

if st.button("1: Arduino Project Handbook Volume 1- Project 0"):
    display_page = ardProj0
if st.button("2: Arduino Project Handbook Volume 1- Project 1"):
    display_page = ardProj1
if st.button("3: Arduino Project Handbook Volume 1- Project 2"):
    display_page = ardProj2

st.markdown(display_page, unsafe_allow_html = True)

if st.button("Close Notes"):
    display_page = ""