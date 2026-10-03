# Tibia_Learns_Things

This is a streamlit meant ot document my journey into learning topics such as electronics and game design (among other things).

## Making the website

### streamlit-option-menu

My original prototype had a horizontal navigation bar up top using the `streamlit-option-meunu` library but it wasn't quite working the way I wanted it to so I have to default back to the typical streamlit sidebar.

### The original prototype didn't cut it anymore

My pipeline isn't always the greatest so my lofi prototype on penpot often acts as a sketch you get in charettes. Because of some streamlit bugs (streamlit couldn't find pages) I encountered, I had to change the format of the website.

### Uploading markdown files

Pathlib wasn't working for me as a way to upload the files so I ended up going for the native open() from python.

### Displaying the markdown files properly

I started off the Electronics note page like this:

```
import streamlit as st
#from pathlib import Path
from functionality import read_markdown_file

st.title("Electronics Notes")

st.write("Click on any part of the table of contents below to open up a topic to read about. There will be a close button at the bottom of each section when you're done reading.")

st.header("Table of Contents")

md_path_01 ="pages/topic_notes/markdown/useful_links.md"
useful_links = read_markdown_file(md_path_01)

md_path_02 = "pages/topic_notes/markdown/electronics_self_teaching.md"
electronics_self_teaching = read_markdown_file(md_path_02)

#button links

if st.button("1: Useful Links", key="useful-links"):
    st.session_state.active_context = st.markdown(useful_links, unsafe_allow_html=True)
    if st.button("Close this section"):
        st.session_state.active_context = None

if st.button("2: Electronics Self Teaching Guide", key="electronics-self-teaching"):
    st.session_state.active_context = st.markdown(electronics_self_teaching, unsafe_allow_html=True)
    if st.button("Close this section"):
        st.session_state.active_context = None
#what makes the markdown show up:
#st.markdown(useful_links, unsafe_allow_html=True)

```

But I wasn't sure if that would work UI-wise. So I'm testing different ways to display the notes effectively. The system I went with is adding an extra variable for displaying which page. This lets the user click a button in the table of contents and that will display the appropriate topic notes. This is the code:

```
import streamlit as st
#from pathlib import Path
from functionality import read_markdown_file

st.title("Electronics Notes")

st.write("Click on any part of the table of contents below to open up a topic to read about.")

st.header("Table of Contents")

md_path_01 ="pages/topic_notes/markdown/useful_links.md"
useful_links = read_markdown_file(md_path_01)

md_path_02 = "pages/topic_notes/markdown/electronics_self_teaching.md"
electronics_self_teaching = read_markdown_file(md_path_02)

display_page = ""

#button links
if st.button("1: Useful Links", key="useful-links"):
    display_page = useful_links

if st.button("2: Electronics Self Teaching Guide", key="electronics-self-teaching"):
    display_page = electronics_self_teaching

#what makes the markdown show up:
#st.markdown(useful_links, unsafe_allow_html=True)
st.markdown(display_page, unsafe_allow_html=True)

```
