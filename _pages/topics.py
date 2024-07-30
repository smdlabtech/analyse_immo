import streamlit as st
import os
import re
import latexifier
import base64
from pathlib import Path
from PIL import Image



def extract_image_links(markdown_content):
    """Attempts to extract image links from the Markdown content, considering the presence or absence of width attribute."""
    # First attempt: Match when the width attribute is empty
    pattern_no_width = r'<img\s+[^>]*?width=""[^>]*?src="(.*?)"'
    links_with_no_width = re.findall(pattern_no_width, markdown_content)
    
    # If no link was found with the width attribute empty, try the second regular expression
    if not links_with_no_width:
        # Using Regex to keep image Links
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

def find_markdown_files(directory):
    """Finds all Markdown files in the given directory and its subdirectories,
    calculates the number of lines for each file, and returns a list of tuples
    containing the file name without extension, number of lines, and full file path."""
    markdown_info = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith('.md'):
                full_path = os.path.join(root, name)
                num_lines = count_lines_in_file(full_path)
                file_name_no_ext = os.path.splitext(name)[0]
                markdown_info.append((file_name_no_ext, num_lines, full_path))
    return sorted(markdown_info, key=lambda x: x[0])

def list_subdirectories(directory):
    """Lists all subdirectories in a given directory."""
    return sorted([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])


#---------------#
# MAIN 
#---------------#
def page_topics():
    """Displays the review page with options to select a module/Topic, subfolder, and Markdown file."""

    st.markdown("<h1 style='text-align: center;'>📖 Topics</h1>", unsafe_allow_html=True)
    st.write("---")

    # Path to the root directory of the courses
    root_directory = "_topics"

    # List of subdirectories (modules/Topics)
    subdirectories = list_subdirectories(root_directory)
    selected_subdirectory = st.selectbox("Choose a Topic", subdirectories)

    if selected_subdirectory:
        selected_directory = os.path.join(root_directory, selected_subdirectory)

        # List of subdirectories in the selected module/Topic
        sub_subdirectories = list_subdirectories(selected_directory)
        selected_sub_subdirectory = st.selectbox("Choose a Module", sub_subdirectories)

        if selected_sub_subdirectory:
            final_directory = os.path.join(selected_directory, selected_sub_subdirectory)

            # Find all Markdown files in the selected subfolder and its subdirectories
            markdown_info = find_markdown_files(final_directory)

            if markdown_info:
                # Create a list of file names for the dropdown menu
                file_names = [info[0] for info in markdown_info]
                selected_file_name = st.selectbox("Choose a File", file_names)

                # Find the information of the selected file
                selected_info = next((info for info in markdown_info if info[0] == selected_file_name), None)

                if selected_info:
                    _, num_lines, full_file_path = selected_info
                    st.write(f"Total rows : {num_lines}")
                    display_markdown_with_images(full_file_path)
            else:
                st.error("No Markdown files found in the specified directory.")
        else:
            st.error("No subfolders found in the specified directory.")
    else:
        st.error("No modules/Topics found in the specified directory.")



#-------------------------#
# Main function
#-------------------------#
if __name__ == "__main__":
    page_topics()
