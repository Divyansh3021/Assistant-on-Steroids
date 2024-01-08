import streamlit as st

# Initialize an empty list to store to-do items
todo_list = []

# Title for the app
st.title("To-Do List")

# Add a text input for new items
new_item = st.text_input("Add a new item:")

# If a new item is entered, append it to the list
if new_item:
    todo_list.append(new_item)

# Display the current to-do list
st.write("Your To-Do List:")
for item in todo_list:
    st.write(item)

# Checkbox for marking items as completed
if st.checkbox("Mark as completed"):
    # Remove the checked item from the list
    todo_list.pop()
