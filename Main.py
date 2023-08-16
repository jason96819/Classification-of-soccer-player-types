import streamlit as st

# Custom imports 
from multipage import MultiPage
from modules import 1_mainmain, 2_role_desc, 3_chatbot_desc, 4_clustering_desc, 5_image_clf_desc, 6_role_clf_desc, 7_searching_desc

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("축구 역할 분류 시스템")

# Add all your applications (pages) here
app.add_page('Main', 1_mainmain.app)
app.add_page('Role Description', 2_role_desc.app)
app.add_page('Chatbot Description', 3_chatbot_desc.app)
app.add_page('Clustering Description', 4_clustering_desc.app)
app.add_page('Image Classification Description', 5_image_clf_desc.app)
app.add_page('Role Classification Description', 6_role_clf_desc.app)
app.add_page('Player Searching Description', 7_searching_desc.app)

# The main app
app.run()
