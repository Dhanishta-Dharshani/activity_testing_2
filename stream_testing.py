import streamlit as st
st.title("Planz - The Perfect Planner")

# multi select box
# first argument takes the box title second argument takes the options to show
hobbies = st.multiselect("Productive activity: ",
                         ['Studies', 'Exrecise', 'Errands'])

# write the selected options
st.write("You have selected", len(hobbies), 'activities')

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter the number of hours you would like to study for: ", "")

# Create a button, that when clicked, shows a text
if(st.button("Submit")):
    st.text("Thank you!")
