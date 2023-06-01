import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    iris = pd.read_csv('iris.csv')
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
    for species in filtered_data['species'].unique():
        species_data = filtered_data[filtered_data['species'] == species]
        plt.hist(species_data[selected_feature], bins=10, alpha=0.5, label=species)
    plt.xlabel(selected_feature)
    plt.ylabel("Count")
    plt.legend()
    st.pyplot()

elif plot_type == 'Boxplot':
    selected_feature = st.sidebar.selectbox("Select Feature", iris.columns[:-1])
    st.subheader("Boxplot")
    plt.boxplot([filtered_data[filtered_data['species'] == species][selected_feature] for species in filtered_data['species'].unique()],
                labels=filtered_data['species'].unique())
    plt.xlabel("Species")
    plt.ylabel(selected_feature)
    st.pyplot()

elif plot_type == 'Scatterplot':
    x_feature = st.sidebar.selectbox("Select X-axis Feature", iris.columns[:-1])
    y_feature = st.sidebar.selectbox("Select Y-axis Feature", iris.columns[:-1])
    st.subheader("Scatterplot")
    for species in filtered_data['species'].unique():
        species_data = filtered_data[filtered_data['species'] == species]
        plt.scatter(species_data[x_feature], species_data[y_feature], label=species)
    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    plt.legend()
    st.pyplot()
