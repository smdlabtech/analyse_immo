import streamlit as st
import app_styles as app_styles

#---------------------#
# Page : "aboutme.py"
#---------------------#

def create_clickable_image(image_path, link, alt_text, style="width:100%;"):
    """
    Crée un HTML pour une image cliquable qui redirige vers un lien donné.

    :param image_path: Chemin vers l'image.
    :param link: URL vers laquelle l'image redirige.
    :param alt_text: Texte alternatif pour l'image.
    :param style: Style CSS pour l'image.
    """
    html_code = f"""
    <a href="{link}" target="_blank">
        <img src="{image_path}" alt="{alt_text}" style="{style}">
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def create_icon_link(icon_class, link, color, size="2x"):
    """
    Crée un HTML pour une icône cliquable qui redirige vers un lien donné.

    :param icon_class: Classe de l'icône (par exemple, "fab fa-linkedin").
    :param link: URL vers laquelle l'icône redirige.
    :param color: Couleur de l'icône.
    :param size: Taille de l'icône (par exemple, "2x").
    """
    html_code = f"""
    <a href="{link}" target="_blank">
        <i class="{icon_class} fa-{size}" style="color:{color};"></i>
    </a>
    """
    return html_code



#-------------------#
# Page : "aboutme.py"
#-------------------#
def page_aboutme():
    st.markdown("<h1 style='text-align: center;'>😎About Me</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Inclure le lien vers la bibliothèque Font Awesome
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Afficher l'image avec app_styles
    st.subheader("✨Data Scientist✨")     # Ajouter les icônes côte à côte    
    st.markdown("""
        👋 Hi, I'm Daya
        I'm like to play soccer and basketball too.  
        I'm passionate about Business Intelligence, data science and programming through the languages :
        Python, R, SQL, Javascript and tools like Power BI, Shiny, Streamlit, Excel VBA and Google Sheets (via Google Apps Script).
        And love working on topics of : Web Scraping, Chatbot Assistant, Text Mining & NLP and Web App Machine Learning, Deep Learning and AI Assistant. ⭐
    """, unsafe_allow_html=True)

    # Générer le HTML pour les icônes
    linkedin_icon = create_icon_link("fab fa-linkedin", "https://www.linkedin.com/in/dayasylla/", "#0e76a8")
    github_icon = create_icon_link("fab fa-github", "https://github.com/smdlabtech", "black")

    # Ajouter les icônes côte à côte
    st.markdown(f"""
    <div style="display: flex; justify-content: left; gap: 10px;">
        {linkedin_icon}
        {github_icon}
    </div>
    """, unsafe_allow_html=True)



#------------------------#
#       MAIN 
#------------------------#
if __name__ == "__main__":
    page_aboutme()
