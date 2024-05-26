import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Seitenkonfiguration muss zuerst gesetzt werden
st.set_page_config(page_title="Iris Dataset Explorer")

# Laden des Datensets
@st.cache
def load_data():
    return sns.load_dataset('iris')

df = load_data()

# Überschrift
st.title('Iris Dataset Explorer')

# Interaktive Widgets
species_option = st.multiselect('Welche Iris-Spezies anzeigen?', df['species'].unique(), default=df['species'].unique())
display_option = st.radio("Datenanzeige Option:", ('Tabelle', 'Diagramm'))

# Datenanzeige
if display_option == 'Tabelle':
    st.write(df[df['species'].isin(species_option)])
else:
    fig, ax = plt.subplots()
    for species in species_option:
        subset = df[df['species'] == species]
        ax.scatter(subset['sepal_length'], subset['sepal_width'], label=species)
    plt.legend(title='Spezies')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Sepal Length vs Width nach Spezies')
    st.pyplot(fig)

# Seitenfuss
st.write('Anzahl der angezeigten Datenpunkte:', len(df[df['species'].isin(species_option)]))
