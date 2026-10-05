import streamlit as st

st.title("Electronics Project Ideas")
st.write("This page is just to catalogue project ideas that I think " \
"would be cool to make once I have enough knowledge under the belt, "
"or when I've reviwed enough of a topic I've seen before (like software development). " \
"I've separated them by topic.")

st.divider()

st.header("Electronics")
st.subheader("1. E-reader")
st.write("I've always been a fan of e-readers ever since Barnes N Noble had their Nook. " \
"Mine broke but I have a Kindle now. I'd like to get something with an E-Ink Display again so what better way" \
" then to try to build my own. A smaller one would help in portability too. The Xteink X series pocket eraders are a" \
" good model to go by since they're ESP32 based from what I've heard.")

st.subheader("2. V-Pet")
st.write("My sister has become an avid tamagochi enthusiast, rekindling a childhood interest in them. I can't lie," \
"the game play has a nice cozyness to them, so it would be cool to make one, or even just make this a feature on another device.")

st.subheader("3. Music Player")
st.write("This is part of my effort to decentralize my life from my phone. Part of how I use mine is a portable music player so if I can make" \
"an mp3 player where I can customize the music more like how old mp3 players worked, I can get away from my phone more.")

st.subheader("4. Thermal Print Camera")
st.write("I saw someone online make one and it didn't look too complicated. I bought one off depop (it's a toy) and have fun with it," \
"so if I can make my own that'd be cool. From what I saw the components were: a PCB (duh), a power source, a thermal printer and of course a case (the girl online used a shoebox because it was a temporary demo). ")

st.subheader("5. Paul Lagier's Quest Cam")
st.write("One of Paul Lagier's projects on his youtube channel show him making a mini digital camera that also gives users a quest (you have to take pictures " \
"to fufill that quest). He often provides instructions and materials lists on his ko-fi to encourage his viewers to make the projects himself. As of writing this" \
" I have not seen the instructions for this project on his ko-fi yet, but this project really appeals to me so I'm looking forward to it.")

st.subheader("6. Weather checker")
st.write("I've noticed that it's not the most common habit to check the weather in the morning, and I'm sick of using the google machines to check anyway," \
"so having a little keychain or trinket with the sole purpose of checking the weather just seems nice. Although this could be a feature on a mini cyber deck (inspired by nashallery's little cyberdeck.)")

st.subheader("7. Digital Camera")
st.write("I just think it'd be fun. I like photography as a hobby and I've seen good camera uses that would help me get out of the house. Plus I think it'd be cool to make my own camera.")

st.divider()

st.header("Game design")
st.subheader("1. Text based adventures using my Madness In a Bottle Story")
st.write("A text-based games will allow me to think about mechanics like game loops without worrying" \
"about making art assets too much, and I can still have fun with it because I can use my own stories to add " \
"interactivity to them. ")

st.divider()

st.header("Software Development")
st.subheader("1. Screen Time Measuring Web App")
st.write("The goal of this app is just data display." \
"This app would allow users to enter in their daily screen time on their phones. " \
"From that, there will be a graph to track daily screen time over time. " \
"I think it'd be funny to include this option: if the user's screen time is 8 hours or more, " \
"the app will give the user a list of hobbies to try. Streamlit will be a convenient library for data " \
"display, but the tedious part will making the app look cute.")

st.subheader("2. Quest Cam App")
st.write("This is inspired by Paul Lagier's questcam project (on youtube). " \
"The goal would be the app would give you a quest, and you can upload photos to each quest " \
"to complete it. I don't know yet if the quest should be given on command (like at the press of a button) or it gives you a daily one yet. " \
"It could have a gallery to see past quest and their desginated photos. " \
"I'm also still debating on what language to use. Should it be electron, godot, or streamlit? Or even something else. ")

st.divider()


