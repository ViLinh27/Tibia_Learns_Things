import streamlit as st
from functionality import read_markdown_file

st.title("Electronics Projects")

st.header("Table of Contents")

md_path_01 = "pages/topic_projects/markdown/1_ArduinoProjectHandbook_p00.md"
ardProj0 = read_markdown_file(md_path_01)

md_path_02 = "pages/topic_projects/markdown/2_ArduinoProjectHandbook_p01.md"
ardProj1 = read_markdown_file(md_path_02)

md_path_03 = "pages/topic_projects/markdown/3_ArduinoProjectHandbook_p02.md"
ardProj2 = read_markdown_file(md_path_03)

md_path_04 = "pages/topic_projects/markdown/4_ArduinoProjectHandbook_p03.md"
ardProj3 = read_markdown_file(md_path_04)

md_path_05 = "pages/topic_projects/markdown/5_ArduinoProjectHandbook_p04.md"
ardProj4 = read_markdown_file(md_path_05)

display_page = ""

if st.button("1: Arduino Project Handbook Volume 1- Project 0"):
    display_page = ardProj0
if st.button("2: Arduino Project Handbook Volume 1- Project 1"):
    display_page = ardProj1
if st.button("3: Arduino Project Handbook Volume 1- Project 2"):
    display_page = ardProj2
if st.button("4: Arduino Project Handbook Volume 1- Project 3"):
    display_page = ardProj3
if st.button("5: Arduino Project Handbook Volume 5- Project 4"):
    display_page = ardProj4
    
st.markdown(display_page, unsafe_allow_html = True)

if st.button("Close Project"):
    display_page = ""