import streamlit as stm
stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")

from streamlit_card import card
stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")
card(
    title="Hello Geeks!",
    text="Click this card to redirect to GeeksforGeeks",
    image="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190710102234/download3.png",
    url="https://www.geeksforgeeks.org/",
)


from streamlit_extras.stodo import to_do
stm.set_page_config(page_title="This is a Simple Streamlit WebApp")
stm.title("This is the Home Page Geeks.")
stm.text("Geeks Home Page")
to_do(
    [(stm.write, "<may or may not add emoji or\
    shortcode here> Get Up Early")],
    "coffee",
)
to_do(
    [(stm.write, "<may or may not add emoji or shortcode \
    here> Eat a healthy Breakfast")],
    "pancakes",
)
to_do(
    [(stm.write, ":computer: Start solving\
    Problems on GeeksforGeeks!")],
    "work",
)

