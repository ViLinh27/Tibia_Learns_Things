import streamlit as st
from streamlit_option_menu import option_menu  
from functionality import read_markdown_file

st.title("Game Design Projects")

st.header("Table of Contents")

md_path_01 = "pages/topic_projects/markdown/001_TxtBasedGame_Miab.md"
gdProj1 = read_markdown_file(md_path_01)

display_page = ""

if st.button("1: Text Based Adventure Game Madness In a Bottle"):
    display_page = gdProj1

st.markdown(display_page,unsafe_allow_html=True)

if st.button("Close Project"):
    display_page = ""