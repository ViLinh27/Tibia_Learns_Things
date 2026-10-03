import streamlit as st

pages = {
    "": [
        st.Page("pages/homepage.py", title="Home"),
        st.Page("pages/about.py", title="About"),
        st.Page("pages/notes.py", title="Notes"),
        st.Page("pages/projects.py", title="Projects"),
        st.Page("pages/links.py", title="Links"),
        st.Page("pages/contact.py", title="Contact"),
    ],
}

pagesrunner = st.navigation(pages)

pagesrunner.run()