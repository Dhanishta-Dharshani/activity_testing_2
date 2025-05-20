import streamlit as st
st.title("Planz - The Perfect Planner")

hobbies = st.multiselect("Productive activities: ",
                         ['Studies', 'Exrecise', 'Errands'])
st.write("You have selected", len(hobbies), 'activities')

name = st.text_input("Enter the number of hours you would like to do the productive activity for: ", "")

if(st.button("Submit")):
    st.text("Thank you!")
