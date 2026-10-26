import streamlit as st

st.title("About")

#who am i image and text blurb here
st.header("Who am I?")

st.image("https://res.cloudinary.com/wjd2npkc/image/upload/v1793027005/dogLOGO.png",width=250);

st.write("""
    Hello! It's nice to meet you visitor. My name is Linh. I am a digital artist who likes to draw and write things. 
    I graduated with a masters in computer science but had difficulty finding work in that field due to the rise of AI dependency ( and subsequent misuse)
    Coding has always been fun for me in a lot of ways. It's still a creative outlet and I try to make things likeminded people could find useful.
""")
#what is this site used for text blurb here

st.header("What is this site for?")
st.write("""
    I've been seeing a rise in women getting into hardware and giving tech a very whimsical makeover. It's been super cool to see.
    Additionally, there's been an increase in digital fatigue due to the consolidation of tasks onto mobile phones and increase in subscriptions. 
    The software field's increasing reliance on generative AI doesn't help in that digital fatigue either. 
         
    Hardware has allowed people to decentrilize themselves from their phones.
    So I wanted to be part of that effort into making hardware more whimsy. Tech's new cute look has really appealed to me so it's motivating me to learning it 
    (to the surprise of my electrical engineer father).
    Lastly, I'd like this website to be a learning resource for anyone else who wants to get into hardware or whatever topic that's on the nav bar. It's cool to learn things.
""")

st.subheader("Some of the original notes I had when conceptualizing this website")
st.write(""" - Similar to youtube girl using channel to show herself teaching electronics, I could make a site to show me learning electronics
- Site to document learning game design
    - include process of game making?
    - text based -> graphic
- site to learn game engines/ Damarjian's youtube videos?
    - he has video tutorial playlists
- can document projects on circuit sims too
- react or vanilla?
- streamlit?
- another topic to approach aside from electronics & game design is reviewing Java fundamentals with that OReilly SW dev proj book
- Consider having section for resources so people know what to use
    - from books
    - youtube channels
    - IG accounts
- Consider having section for cool project goals as a way to catalogue what would be cool to make
    - e-reader
    - thermal print cam
    - v pet
    - Paul Lagier's quest-cam
    - music player
    - weather checker
    - standard digi-cam
         
- Nashallery has these (vpet, music player, weather checker) as features on 1 cyberdeck
         """)