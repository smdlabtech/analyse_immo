import streamlit as st
import pandas as pd
import app_styles

# Exemple de DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Titre de l'application
st.title('Exemple de Filtre de Liste Déroulante dans Streamlit')

# Liste déroulante pour sélectionner une ville
selected_city = st.selectbox('Sélectionnez une ville:', df['City'].unique())

# Filtrer le DataFrame en fonction de la sélection
filtered_df = df[df['City'] == selected_city]

# Afficher les résultats filtrés
st.write('Résultats filtrés:')
st.dataframe(filtered_df)



with st.sidebar:
    app_styles.load_img("senlab_ia_gen_rmv_bgrd.png", caption="🇸🇳 SenLab IA 🇫🇷", width=5, use_column_width=True, output_format='PNG')
    st.sidebar.markdown("<h1 style='text-align: left; color: grey;'>Sidebar Panel : </h1>", unsafe_allow_html=True)
    
    app_styles.load_img("logo-brsma-rmvbg.png", caption="", width=5, use_column_width=True, output_format='PNG', link="https://clients.boursobank.com/connexion/saisie-mot-de-passe")
    st.sidebar.markdown("<h1 style='text-align: left; color: grey;'>Sidebar Panel : </h1>", unsafe_allow_html=True)
    
    app_styles.load_img("logo-lcl-rmvbg.png", caption="", width=5, use_column_width=True, output_format='PNG', link="https://monespace.lcl.fr/connexion")
    st.sidebar.markdown("<h1 style='text-align: left; color: grey;'>Sidebar Panel : </h1>", unsafe_allow_html=True)