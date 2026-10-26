import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles/mainstyles.css")

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
        st.Page("pages/topic_notes/swdesign_notes.py", title="Software Dev Notes")
    ],
    "Projects":[
        st.Page("pages/topic_projects/electronics_projects.py", title="Electronics Projects"),
        st.Page("pages/topic_projects/game_design_projects.py", title="Game Design Projects"),
        st.Page("pages/topic_projects/swd_projects.py",title="Software Dev Projects")
    ],
    "Resources":[
        st.Page("pages/resources_books.py",title="Books by Topic"),
        st.Page("pages/resources_ytchannels.py",title="Youtube Channels by Topic"),
        st.Page("pages/resources_misc.py", title="Miscellaneous Resources by Topic")
    ],
    "Project Ideas / Goals": [
        st.Page("pages/project_ideas_electronics.py", title="Electronics Ideas"),
        st.Page("pages/project_ideas_gameDesign.py", title="Game Design Ideas"),
        st.Page("pages/project_ideas_swDev.py", title="Software Development Ideas")
    ]
}

pagesrunner = st.navigation(pages)

pagesrunner.run()