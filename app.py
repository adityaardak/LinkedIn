import pandas as pd
import numpy as np
import streamlit as st


# Title
st.title("Streamlit Text Display Example")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a simple text.")

# Markdown
st.markdown("# Markdown Title")
st.markdown("## Markdown Header")
st.markdown("*This is italic text* and **this is bold text**.")

# Write
st.write("This is a text written using `st.write`.")
st.write("Use it to display **bold**, *italic*, or even `code` inline.")

# Text Input
user_input = st.text_input("Enter your name:")
st.write("You entered:", user_input)



st.title("Map Visualization")

# Generate random geographical data
df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# Display the map
st.map(df)
