import streamlit as st
import pandas as pd

# Dummy dataframe for example purposes
data = {
    'message': [
        'Hello world',
        'This is a test message',
        'Another test message',
        'Hello again'
    ]
}
df = pd.DataFrame(data)

def particularword(selected_word, df):
    # Initialize an empty dictionary
    my_dict = {}

    # Iterate over the rows of the dataframe
    for index, message in pd.DataFrame[df['message']].iteritems():
        # Check if the selected word is in the message
        if selected_word.lower() in message.lower().split():
            # Add the message and its index to the dictionary
            my_dict[message] = index

    return my_dict

# Sidebar for text input
title = st.sidebar.text_input("Enter some text 👇", placeholder="Enter Here.")

# Process and display results
if title:
    my_dict = particularword(title, df)
    if my_dict:  # Check if there are any results
        newdf = pd.DataFrame(list(my_dict.items()), columns=['Message', 'Index'])
        st.dataframe(newdf)
    else:
        st.sidebar.write("No messages found containing the text.")
else:
    st.sidebar.write("Please enter some text to see results.")
