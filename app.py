import streamlit as st
import pandas as pd

st.title('CSV Data exploration with Github')
text_data = st.text_input('Your github url', "", placeholder="e.g., https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv")
if text_data == "":
    st.info("We didn't receive any data, please type your github url in text box")
else:
    st.subheader("CSV data")
    df = pd.read_csv(text_data)
    st.write(df)
