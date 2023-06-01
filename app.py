import streamlit as st
import pandas as pd
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    iris = sns.load_dataset('iris')
    return iris

iris = load_data()

# Set up the Streamlit app
st.title("Iris Dataset Visualization")

# Add checkboxes to select species
selected_species = st.sidebar.multiselect("Select Species", iris['species'].unique())

# Apply species filter
filtered_data = iris[iris['species'].isin(selected_species)]

# Display filtered dataset
st.subheader("Filtered Dataset")
st.write(filtered_data)

# Visualization options
plot_type = st.sidebar.selectbox("Select Plot Type", ['Histogram', 'Boxplot', 'Scatterplot'])

# Generate plot based on selected type
if plot_type == 'Histogram':
    selected_feature = st.sidebar.selectbox("Select Feature", iris.columns[:-1])
    st.subheader("Histogram")
    sns.histplot(data=filtered_data, x=selected_feature, hue='species', kde=True)
    st.pyplot()

elif plot_type == 'Boxplot':
    selected_feature = st.sidebar.selectbox("Select Feature", iris.columns[:-1])
    st.subheader("Boxplot")
    sns.boxplot(data=filtered_data, x='species', y=selected_feature)
    st.pyplot()

elif plot_type == 'Scatterplot':
    x_feature = st.sidebar.selectbox("Select X-axis Feature", iris.columns[:-1])
    y_feature = st.sidebar.selectbox("Select Y-axis Feature", iris.columns[:-1])
    st.subheader("Scatterplot")
    sns.scatterplot(data=filtered_data, x=x_feature, y=y_feature, hue='species')
    st.pyplot()
