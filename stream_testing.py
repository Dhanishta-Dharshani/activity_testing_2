import streamlit as st
st.title("Hello World")
# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Productive Time: ",
                     ['Studies', 'Exercise', 'Errands'])

# print the selected hobby
st.write("The productive activity that you have chosen is: ", hobby)
