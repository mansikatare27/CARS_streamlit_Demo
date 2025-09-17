import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv("../Datasets/Cars.csv")

# Set the Streamlit app title
st.title("Car Brand Horsepower Visualizer")

# Show raw data if checkbox is selected
if st.checkbox("Show raw data"):
    st.write(df)

# Get unique car makes
car_makes = sorted(df['Make'].dropna().unique())

# Dropdown menu to select car make
selected_make = st.selectbox("Select a Car Brand", car_makes)

# Filter dataframe based on selected make
filtered_df = df[df['Make'] == selected_make]

# Check if data is available for selected make
if not filtered_df.empty:
    st.write(f"Showing data for: **{selected_make}**")
    st.write(filtered_df)

    # Create the plot
    plt.figure(figsize=(10, 5))
    sns.barplot(x=filtered_df['Make'], y=filtered_df['Horsepower'])

    plt.title(f"Horsepower of {selected_make} Cars")
    plt.xticks(rotation=90)

    # Display the plot in Streamlit
    st.pyplot(plt)
else:
    st.warning(f"No data available for '{selected_make}'")
