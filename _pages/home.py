import streamlit as st
import base64
import re
import os
import app_styles as app_styles
# from _pages 




def extract_image_links(markdown_content):
    """Attempts to extract image links from the Markdown content, considering the presence or absence of width attribute."""
    # First attempt: Match when the width attribute is empty
    pattern_no_width = r'<img\s+[^>]*?width=""[^>]*?src="(.*?)"'
    links_with_no_width = re.findall(pattern_no_width, markdown_content)
    
    # If no link was found with the width attribute empty, try the second regular expression
    if not links_with_no_width:
        pattern_any_width = r'<img\s+[^>]*?src="(.*?)"'
        links_with_any_width = re.findall(pattern_any_width, markdown_content)
    
    # Combine the results of both attempts
    all_links = links_with_no_width + links_with_any_width
    
    return all_links


def load_and_encode_image(image_path):
    """Loads an image from the specified path and encodes it in Base64."""
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode()
    return encoded_image

def insert_images_into_markdown(markdown_content, image_links, base_path):
    """Inserts Base64 encoded images into the Markdown content."""
    for link in image_links:
        # Build the absolute path of the image
        img_path = os.path.join(base_path, link)
        if os.path.isfile(img_path):
            img_encoded = load_and_encode_image(img_path)
            img_html = f'data:image/jpeg;base64,{img_encoded}'
            markdown_content = markdown_content.replace(link, img_html)
    return markdown_content

def display_markdown_with_images(markdown_file_path):
    """Reads the content of a Markdown file and inserts images."""
    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
            base_path = os.path.dirname(markdown_file_path)
            image_links = extract_image_links(markdown_content)
            markdown_content = insert_images_into_markdown(markdown_content, image_links, base_path)
            st.markdown(markdown_content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"The Markdown file '{markdown_file_path}' was not found.")

def count_lines_in_file(file_path):
    """Returns the number of lines in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)


#-------------#
# "homepage.py"
#-------------#
def page_home():
    # st.title("🏠Home")
    st.markdown("<h1 style='text-align: center;'>🏠Home</h1>", unsafe_allow_html=True)
    st.write("---")
    # app_styles.display_markdown("home_explained.md")
    app_styles.display_markdown("home_explained.md")
    # st.write("**Home :**")
