import pandas as pd
import streamlit as st
import os
from glob import glob
import json


# Dans app_data_loader.py ou dans le même fichier que votre application Streamlit
def load_files_json(filepath):
    """
    Loads the contents of a JSON file.
    
    Args:
    filepath (str): The path to the JSON file.
    
    Returns:
    dict: The contents of the JSON file in dictionary form.
    """
    with open(filepath, 'r') as file:
        return json.load(file)


# @st.cache
def load_quiz_json(file_path):
    """
    Load questions and answers from a Markdown file.
    
    Args:
    file_path (str): The path to the Markdown file.
    
    Returns:
    dict: A dictionary containing the questions and their answers.
    """
    questions = []
    answers = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('Q:'):
                question_text = line[2:].strip()
                question_id = len(questions)
                questions.append(question_text)
                answers[question_id] = None  # The answer will be set later
            elif line.startswith('A:'):
                answer_text = line[2:].strip()
                question_id = int(line.split(':')[0].split('.')[0]) - 1  # Assuming the question ID starts at 1
                answers[question_id] = answer_text
    return questions, answers





## load_markdown__quiz
# @st.cache
def load_quiz_markdown(file_name):
    """
    Load the content of a Markdown file for a specific _quiz.
    
    Args: file_name (str): The name of the Markdown file to load.
    
    Returns: str: The content of the Markdown file as a string.
    """
    # Construct the path to the Markdown file using the "_quiz" folder
    base_directory = os.path.dirname(os.path.abspath(__file__))
    quiz_directory = os.path.join(base_directory, "_quiz")
    full_path = os.path.join(quiz_directory, file_name)
    
    # Check if the file exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{full_path}'")
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content  # Return a string representing the content of the Markdown file
    

# @st.cache_data 
def load_files_markdown(file_name):
    """
    Load the content of a Markdown file.
    
    Args: file_name (str): The name of the Markdown file.
    
    Returns: str: The content of the Markdown file as a string.
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_quiz", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_name}' not found at '{file_path}'")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content  # Return a string

