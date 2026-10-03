import streamlit as st

pages = {
    "": [
        st.Page("pages/homepage.py", title="Home"),
        st.Page("pages/about.py", title="About"),
        st.Page("pages/links.py", title="Links"),
        st.Page("pages/contact.py", title="Contact"),
    ],
    "Notes":[
        st.Page("pages/topic_notes/electronics_notes.py", title="Electronics Notes"),
        st.Page("pages/topic_notes/game_design_notes.py", title="Game Design Notes"),
    ],
    "Projects":[
        st.Page("pages/topic_projects/electronics_projects.py", title="Electronics Projects"),
    ]
}

pagesrunner = st.navigation(pages)

pagesrunner.run()