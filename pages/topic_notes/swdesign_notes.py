import streamlit as st
from functionality import read_markdown_file
st.title("Sowftware Development Notes")

st.header("Table of Contents")

md_path_01 = "pages/topic_notes/markdown/0001_SWDOReilly1.md"
oreillybook = read_markdown_file(md_path_01)

display_page = ""

if st.button("1: O'Reilly's Real-World Software Development Ch 1"):
    display_page = oreillybook

st.markdown(display_page, unsafe_allow_html=True)
if st.button("Close Notes"):
    display_page = ""