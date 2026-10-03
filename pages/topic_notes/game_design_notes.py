import streamlit as st
from streamlit_option_menu import option_menu
from functionality import read_markdown_file
st.title("Game Design Notes")

st.header("Table of Contents")

md_path_01 = "pages/topic_notes/markdown/001_gameDesignersHandbook.md"
handbook01 = read_markdown_file(md_path_01)

display_page = ""

if st.button("1: Game Designer's Handbook Series- Book 01"):
    display_page = handbook01

st.markdown(display_page, unsafe_allow_html=True)