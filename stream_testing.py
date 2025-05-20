import streamlit as st
st.title("Planz - The Perfect Planner")

productive = st.multiselect("Productive activities: ",
                         ['Studies', 'Exrecise', 'Errands'])
st.write("You have selected", len(productive), 'activities')

pro_name = st.text_input("Enter the number of hours you would like to do the productive activity for: ", "")


self = st.multiselect("Self-care activities: ",
                         ['Skin care', 'Hair care', 'Journalling'])
st.write("You have selected", len(self), 'activities')

self_name = st.text_input("Enter the number of hours you would like to do the self-care activity for: ", "")

relax = st.multiselect("Relaxation activities: ",
                         ['Hobbies', 'Gadgets'])
st.write("You have selected", len(relax), 'activities')

relax_name = st.text_input("Enter the number of hours you would like to do the productive activity for: ", "")
