import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Title
st.title("Streamlit Example App: Demonstrating Streamlit Features")

# Sidebar
st.sidebar.header("Navigation")
nav = st.sidebar.radio("Go to", ["Home", "Text Display", "Widgets", "Graphs", "Data", "Media", "Progress Bar"])

# Home Section
if nav == "Home":
    st.header("Welcome to the Streamlit App!")
    st.write("This app demonstrates various Streamlit features, including text, widgets, data display, graphs, and media.")
    st.markdown("### Key Features:")
    st.markdown("- Display Text in Different Formats")
    st.markdown("- Use Interactive Widgets like buttons and sliders")
    st.markdown("- Display Data and Charts")
    st.markdown("- Include Media (Images, Audio, and Video)")
    st.markdown("- Track Progress with Progress Bars")

# Text Display Section
if nav == "Text Display":
    st.header("Text Display Examples")
    st.text("This is plain text.")
    st.markdown("### Markdown Example")
    st.markdown("**This is bold text**, *this is italic text*, and `this is code`. \n - This is a bullet point.")
    st.code('st.markdown("This is **Markdown Text**")', language="python")
    st.write("Write can display any object, such as this:", {"key": "value"})

# Widgets Section
if nav == "Widgets":
    st.header("Interactive Widgets")
    # Text Input
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")

    # Slider
    age = st.slider("Select your age:", 0, 100, 25)
    st.write(f"Your age is: {age}")

    # Buttons
    if st.button("Click Me"):
        st.success("You clicked the button!")

    # Checkbox
    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.info("Thanks for agreeing!")

# Graphs Section
if nav == "Graphs":
    st.header("Graph Examples")
    # Line Chart
    st.subheader("Line Chart")
    data = pd.DataFrame(np.random.randn(10, 2), columns=["X", "Y"])
    st.line_chart(data)

    # Bar Chart
    st.subheader("Bar Chart")
    st.bar_chart(data)

    # Matplotlib Chart
    st.subheader("Matplotlib Chart")
    fig, ax = plt.subplots()
    ax.plot(data["X"], data["Y"], marker="o")
    st.pyplot(fig)

# Data Section
if nav == "Data":
    st.header("Data Display")
    # Create a DataFrame
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Age": [25, 30, 35, 40],
        "City": ["New York", "Los Angeles", "Chicago", "Houston"]
    })
    st.write("Static Table")
    st.table(df)
    st.write("Interactive DataFrame")
    st.dataframe(df)

# Media Section
if nav == "Media":
    st.header("Media Files")
    # Image
    st.image("https://via.placeholder.com/300", caption="Sample Image")
    
    # Audio
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    
    # Video
    st.video("https://www.youtube.com/watch?v=9bZkp7q19f0")

# Progress Bar Section
if nav == "Progress Bar":
    st.header("Progress Bar Example")
    st.write("Simulating a task...")
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.05)
        progress_bar.progress(i)
    st.success("Task Completed!")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ using Streamlit")
