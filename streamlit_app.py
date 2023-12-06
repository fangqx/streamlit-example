from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
"""

# Everything is accessible via the st.secrets dict:
headers={"authorization":st.secrets["githubkey"],"content-type":"application/json"}
#st.write("DB username:", st.secrets["db_username"])
#st.write("DB password:", st.secrets["db_password"])
#st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:


st.write('hello world')
st.write('good morning')
st.write('hellooooo')
