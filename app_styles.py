import os
import streamlit as st
from PIL import Image
import io


def styles_img(image_file, caption=None, use_column_width=True, width=None, height=None, output_format=None):
    """
    Loads and displays an image in a Streamlit application.
    
    Args:
    image_file (str): Name of the image file to load.
    caption (str): Optional caption to be displayed below the image.
    use_column_width (bool): Whether or not to use column width for the image.
    width (int): Image width in pixels.
    height (int): Image height in pixels.
    output_format (str): Image output format (e.g. 'PNG', 'JPEG').
    """
    # Construire le chemin complet vers le fichier image en utilisant le nom du fichier passé en argument
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets", "img", image_file)
    return st.image(image_path, caption=caption, use_column_width=use_column_width, width=width, output_format=output_format)


def styles_css(css_file):
    """
    Loads and applies a CSS file to a Streamlit application.
    
    Args:
    css_file (str): Name of CSS file to load.
    """
    # Construire le chemin complet vers le fichier CSS en utilisant le nom du fichier passé en argument
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "css", css_file)
    if not os.path.exists(css_path):
        raise FileNotFoundError(f"File '{css_file}' not found at '{css_path}'")
    
    with open(css_path) as f:
        css = f.read()
    
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def styles_html(file_name):
    """
    Loads HTML content from the given file name.
    
    Args:
    file_name (str): Name of HTML file to load.

    Returns:
    str: HTML content as string.
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "html", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{file_path}'")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def styles_js(file_name):
    """
     Loads JavaScript content from the given filename.
    
    Args:
    file_name (str): Name of JavaScript file to load.

    Returns:
    str: JavaScript content as string.
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "js", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{file_path}'")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content


def styles_md(file_name):
    """
    Loads Markdown content from the given file name.
    
    Args:
    file_name (str): Name of Markdown file to load.

    Returns:
    str: Markdown content as string.
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "markdown", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{file_path}'")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

#---------------------#
def load_css(css_file):
    """
    Charge et applique un fichier CSS à une application Streamlit.
    
    Args:
    css_file (str): Nom du fichier CSS à charger.
    """
    # Construire le chemin complet vers le fichier CSS en utilisant le nom du fichier passé en argument
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "css", css_file)
    if not os.path.exists(css_path):
        raise FileNotFoundError(f"File '{css_file}' not found at '{css_path}'")
    
    with open(css_path) as f:
        css = f.read()
    
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


#-----------------------------#
# MARKDOWN :
#-----------------------------#
def display_markdown(file_name):
    """
    Display Markdown content in a Streamlit application.
    
    Args:
    file_name (str): Name of the Markdown file to load and display.
    
    Returns:
    None
    """
    try:
        markdown_content = load_markdown(file_name)
        st.markdown(markdown_content, unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Error: {e}")



# Read Markdown files
@st.cache_data
def load_markdown(file_name):
    """
    Loads Markdown content from the given file name.
    
    Args:
    file_name (str): Name of the Markdown file to load.

    Returns:
    str: Markdown content as a string.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "assets", "markdown", file_name)
    # file_path = os.path.join(base_path, "assets", "markdown", "assets", "img", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{file_path}'")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content