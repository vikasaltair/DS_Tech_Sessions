#!/usr/bin/env python
# coding: utf-8

# In[1]:

from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_star_rating import st_star_rating
import sqlite3
conn = sqlite3.connect('DS_Tech_Sessions/session_feedback.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS feedback_table(session_date DATE, speaker TEXT, speaker_mail_id TEXT, topic TEXT, date_submitted DATE, Q1 INTEGER, Q2 INTEGER, Q3 TEXT, Q4 TEXT, Q5 TEXT, Q6 TEXT)')

def add_feedback(session_date, speaker, speaker_mail_id, topic, date_submitted, q1, q2, q3, q4, q5, q6):
    c.execute('INSERT INTO feedback_table VALUES (?,?,?,?,?,?,?,?,?,?,?)',(session_date, speaker, speaker_mail_id, topic, date_submitted, q1, q2, q3, q4, q5, q6))
    conn.commit()

# #### Loading Schedule

# In[2]:


#if "schedule_df" not in st.session_state:
 #   st.session_state.schedule_df = pd.read_excel("Schedule.xlsx", skiprows = 2)

session_date = datetime.strptime('2023-04-06', '%Y-%m-%d')
topic = "Team member Recommendation"
speaker = "Vikas Verma"
speaker_mail_id = "vikas.verma@bluealtair.com"
# In[ ]:

st.header('Session Feedback Form')
st.caption("""**_DS Tech sessions are organized once in a week to talk & share individual's knowledge, learning on Data Science & Machine Learning related concepts and techniques.\nSession feedback helps up in analysing program quality/effectiveness, strategies and improvements._**""") 


# ### Creating form 

# In[ ]:
st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 16px;
}
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """<style>
div[class*="stTextInput"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 16px;
}
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """<style>
div[class*="stStarRating"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 16px;
}
    </style>
    """, unsafe_allow_html=True)

st.write("<span style='color:red;'>*</span> Mandatory fields", unsafe_allow_html=True)

with st.form("form1"):
    st.markdown("**1. Was the session interactive & engaging?:red[*]**")
    q1 = st_star_rating(label = '', maxValue = 5, defaultValue = 3, key = "rating-q1", size = 20)
    st.markdown("**2. Was the content useful and interesting?:red[*]**")
    q2 = st_star_rating(label = '', maxValue = 5, defaultValue = 3, key = "rating-q2", size = 20)
    #st.markdown("**3. Speaker's understanding/grasp on the topic***")
    q3 = st.radio("**3. Speaker's understanding/grasp on the topic:red[*]**", ["Poor", "Satisfactory", "Good",  "Excellent"],  key = "rating-q3", index = 2)
    q4 = st.radio("**4. Were your query heard and resolved?:red[*]**", ["Yes", "No"], key = "rating-q4")
    q5 = st.radio("**5. Would you like to have more such sessions?:red[*]**", ["Yes", "No"], key = "rating-q5")
    q6 = st.text_input("**6. Suggestions/Ideas:red[*]**", key = "rating-q6")
    submitted = st.form_submit_button("**Submit**")
    if submitted and q1 and q2 and q3 and q4 and q5 and q6:
        create_table()
        add_feedback(session_date, speaker, speaker_mail_id, topic, datetime.today(), q1, q2, q3, q4, q5, q6)
        st.success('Feedback submitted successfully!')
    else:
        st.error('Please fill out all the required fields')

