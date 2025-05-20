import streamlit as st
st.title("Planz - The Perfect Planner")

productive = st.multiselect("Productive activities: ",
                         ['Studies', 'Exrecise', 'Errands'])
st.write("You have selected", len(productive), 'activities')

name1 = st.text_input("Enter the number of hours you would like to do the productive activity for: ", "")


self = st.multiselect("Self-care activities: ",
                         ['Skin care', 'Hair care', 'Journalling'])
st.write("You have selected", len(self), 'activities')

name2 = st.text_input("Enter the number of hours you would like to do the self-care activity for: ", "")

relax = st.multiselect("Relaxation activities: ",
                         ['Hobbies', 'Gadgets'])
st.write("You have selected", len(relax), 'activities')

name3 = st.text_input("Enter the number of hours you would like to do the productive activity for: ", "")
