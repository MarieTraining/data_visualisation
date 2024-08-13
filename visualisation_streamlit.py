import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the dashboard
st.title("Interactive Data Dashboard")

# Generate sample data
np.random.seed(0)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value': np.random.randn(100)
})

# Sidebar for user input
st.sidebar.header("Filter Options")
selected_category = st.sidebar.selectbox("Select Category", options=data['Category'].unique())

# Filter data based on user input
filtered_data = data[data['Category'] == selected_category]

# Display filtered data
st.write(f"Showing data for category: {selected_category}")
st.dataframe(filtered_data)

# Plotting
st.subheader("Data Visualization")
fig, ax = plt.subplots()
sns.histplot(filtered_data['Value'], kde=True, ax=ax)
ax.set_title(f'Distribution of Values for Category {selected_category}')
st.pyplot(fig)
