import streamlit as st
#from pathlib import Path
from functionality import read_markdown_file

st.title("Electronics Notes")

st.write("Click on any part of the table of contents below to open up a topic to read about.")

st.header("Table of Contents")

md_path_01 ="pages/topic_notes/markdown/1_useful_links.md"
useful_links = read_markdown_file(md_path_01)

md_path_02 = "pages/topic_notes/markdown/2_electronics_self_teaching.md"
electronics_self_teaching = read_markdown_file(md_path_02)

md_path_03 = "pages/topic_notes/markdown/3_electronics_self_teaching-chp01.md"
electronics_self_teaching_01 = read_markdown_file(md_path_03)

display_page = ""

#button links
if st.button("1: Useful Links", key="useful-links"):
    display_page = useful_links

if st.button("2: Electronics Self Teaching Guide Base Knowledge", key="electronics-self-teaching"):
    display_page = electronics_self_teaching


if st.button("3: Electronics Self Teaching Guide Chapter 01", key="electronics-self-teaching-chp01"):
    display_page = electronics_self_teaching_01

#what makes the markdown show up:
#st.markdown(useful_links, unsafe_allow_html=True)
st.markdown(display_page, unsafe_allow_html=True)

if st.button("Close Notes"):
    display_page = ""
