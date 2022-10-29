import streamlit as st
import pandas as pd

st.title('CSV Data exploration with Github')
text_data = st.text_input('Your github url', "", placeholder="e.g., https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv")
st.write(text_data)
