import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st

# Title of the app
st.title("Car Horsepower Viewer by Brand")

# Load the dataset
df = pd.read_csv("Cars.csv")

# Display unique car brands
brands = sorted(df['Make'].dropna().unique())

# Show the list of brands (optional)
st.write("Available Brands:")
st.write(brands)

# Let the user select a brand
selected_brand = st.selectbox("Enter Brand Name:", brands)

# Filter the data based on the selected brand
filtered_df = df[df['Make'] == selected_brand]

# Display filtered data
st.write(f"Filtered data for **{selected_brand}**:")
st.write(filtered_df)

# Plot bar chart
fig, ax = plt.subplots(figsize=(8, 5))
sb.barplot(x=filtered_df.Make, y=filtered_df.Horsepower, ax=ax)
plt.xticks(rotation=90)
ax.set_title(f"Horsepower for {selected_brand}")

# Display the plot in Streamlit
st.pyplot(fig)
