import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données Iris
df = pd.read_csv("iris.csv")

# Configuration de la palette de couleurs "Dusty"
palette = sns.color_palette(["#b56576", "#6d597a", "#355070", "#eaac8b"])

# Titre de l'application
st.title("Blog d'Étude des Fleurs Iris 🌸")

# Sous-titre
st.subheader("Découvrez les caractéristiques des fleurs du célèbre dataset Iris")

# Description du dataset
st.markdown(
    """
    Le dataset **Iris** contient des mesures sur trois espèces de fleurs : *Setosa*, 
    *Versicolor*, et *Virginica*. Ce blog explore leurs caractéristiques, leurs atouts, 
    et leurs inconvénients, à l'aide de visualisations interactives.
    """
)

# Afficher les premières lignes du dataset
st.write("### Aperçu du Dataset")
st.dataframe(df.head())

# Graphique en ligne des mesures
st.write("### Variations des dimensions des fleurs")
feature = st.selectbox("Choisissez une caractéristique :", df.columns[:-1])  # Colonnes sauf la dernière
st.line_chart(df[feature])

# Histogramme des dimensions
st.write("### Distribution des dimensions des fleurs")
fig, ax = plt.subplots()
sns.histplot(data=df, x=feature, hue="species", kde=True, palette=palette, ax=ax)
st.pyplot(fig)

# Afficher les statistiques descriptives
st.write("### Statistiques descriptives")
st.write(df.describe())

# Section FAQ ou blog
st.write("### Blog sur les Fleurs Iris")
st.markdown(
    """
    - **Setosa** : Idéal pour les amateurs de fleurs compactes. 🌿  
      - *Atouts* : Taille petite, facile à cultiver.
      - *Inconvénients* : Moins impressionnante visuellement.
    - **Versicolor** : Un mélange parfait entre taille et élégance. 🌼  
      - *Atouts* : Taille moyenne, couleurs variées.
      - *Inconvénients* : Demande plus de soins.
    - **Virginica** : La plus grande et impressionnante des trois. 🌷  
      - *Atouts* : Grande taille, magnifique pour les jardins.
      - *Inconvénients* : Demande de l'espace.
    """
)
