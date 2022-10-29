import streamlit as st
import pandas as pd

st.title('CSV Data exploration with Github')
text_data = st.text_input('Your github url', "", placeholder="e.g., https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv")
if text_data == "":
    st.info("We didn't receive any data, please type your github url in text box")
else:
    st.header("CSV data")
    #read dataframe
    df = pd.read_csv(text_data)
    st.write(df)
    st.header("Data visualization")
    #line chart
    st.subheader("Visualize from the last column")
    st.line_chart(df.groupby(df.columns[-1]).mean())
    #bar chart
    st.subheader("Filter data from class")
    st.info("Choose a class value")
    #select class from dropdown
    class_value = st.selectbox(
    '',
    df.columns, label_visibility="collapsed")
    st.bar_chart(df.groupby(class_value).mean())
    #simple snow effect
    st.snow()
