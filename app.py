import streamlit as st
import os
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
area = st.text_area("Prompt")
buttonss = st.button("Submit")
if buttonss:
    output = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": area
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    st.write(output.choices[0].message.content)