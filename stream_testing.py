import streamlit as st
st.title("Planz - The Perfect Planner")
# Selection box
# first argument takes the title of the selection box second argument takes options
hobby = st.selectbox("Please choose one productive activity from the following: ",['Select choice','Studies', 'Exercise', 'Errands'])

# print the selected hobby
st.write("The productive activity that you have chosen is: ", hobby)


# multi select box
# first argument takes the box title second argument takes the options to show
hobbies = st.multiselect("Productive activity: ",
                         ['Studies', 'Exrecise', 'Errands'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')



# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("Submit")):
    st.text("Thank you!")



# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter the number of hours you would like to study for: ", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
