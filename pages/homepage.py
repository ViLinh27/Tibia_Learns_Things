import streamlit as st

st.title("Welcome to the Homepage")

st.write("This website is meant to document my journey into learning topics such as electronics and game design (and whatever other topic I find that can help me upskill myself).")
st.write(" I will also be reviewing some software development fundamentals so my skills don't atrophy too much.")
# hero slideshow goes here

#talk bubble with dog goes here
#st.image()
st.divider()
# grid of notes/projects to check out here
st.subheader("Notes")
st.write("Click on a button below to check some of my notes.")
st.page_link("pages/topic_notes/electronics_notes.py", label="Electronics Notes")
st.page_link("pages/topic_notes/game_design_notes.py", label="Game Design Notes")
st.page_link("pages/topic_notes/swdesign_notes.py", label ="Sofware Design Notes")

st.subheader("Projects")
st.write("Click on a button below to check out some of my projects.")
st.page_link("pages/topic_projects/electronics_projects.py", label="Electronics Projects")
st.page_link("pages/topic_projects/game_design_projects.py", label="Game Design Projects")
st.divider()