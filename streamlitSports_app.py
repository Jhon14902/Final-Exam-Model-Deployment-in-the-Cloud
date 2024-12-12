import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load a publicly available sports dataset
# For this demonstration, we will use a sample dataset of basketball player stats
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv" # Replace this with any sports-related dataset

# Load the dataset
data = pd.read_csv(url, names=["Player", "Height (in)", "Weight (lbs)"])

# Streamlit app starts here
st.title("Sports Statistics Viewer")
st.write("Explore sports statistics with filtering and visualization tools.")

# Display the raw data
st.header("Dataset Overview")
st.write("Here's a preview of the dataset:")
st.dataframe(data)

# Filter by height or weight
st.sidebar.header("Filters")
min_height = st.sidebar.slider("Minimum Height (in)", int(data["Height (in)"].min()), int(data["Height (in)"].max()), int(data["Height (in)"].min()))
max_height = st.sidebar.slider("Maximum Height (in)", int(data["Height (in)"].min()), int(data["Height (in)"].max()), int(data["Height (in)"].max()))
min_weight = st.sidebar.slider("Minimum Weight (lbs)", int(data["Weight (lbs)"].min()), int(data["Weight (lbs)"].max()), int(data["Weight (lbs)"].min()))
max_weight = st.sidebar.slider("Maximum Weight (lbs)", int(data["Weight (lbs)"].min()), int(data["Weight (lbs)"].max()), int(data["Weight (lbs)"].max()))

filtered_data = data[(data["Height (in)"] >= min_height) &
                     (data["Height (in)"] <= max_height) &
                     (data["Weight (lbs)"] >= min_weight) &
                     (data["Weight (lbs)"] <= max_weight)]

st.header("Filtered Data")
st.write(filtered_data)

# Visualization
st.header("Height vs Weight")
fig, ax = plt.subplots()
ax.scatter(filtered_data["Height (in)"], filtered_data["Weight (lbs)"], c="blue", alpha=0.7)
ax.set_title("Height vs Weight")
ax.set_xlabel("Height (inches)")
ax.set_ylabel("Weight (lbs)")
st.pyplot(fig)

# End of the app
st.write("---")
st.write("Built with Streamlit")
