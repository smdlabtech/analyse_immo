import streamlit as st
import os
import json

# Function for loading quiz JSON files
def list_quiz_files(directory, subdirectory=None):
    """
    Lists JSON files in a directory and its subdirectory.

    Args:
        directory (str): The path to the directory containing quiz files.
        subdirectory (str): The subdirectory (theme/module) to list JSON files from.

    Returns:
        list: A list of JSON files in the directory or subdirectory.
    """
    if subdirectory:
        directory = os.path.join(directory, subdirectory)
    return sorted([f for f in os.listdir(directory) if f.endswith('.json')])

# Function for listing themes (subdirectories)
def list_themes(directory):
    """
    Lists subdirectories in a directory.

    Args:
        directory (str): The path to the directory containing themes.

    Returns:
        list: A list of subdirectories (themes) in the directory.
    """
    return sorted([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])

def select_theme_module_and_quiz(quiz_directory):
    """
    Allows user to select a theme, then a module within that theme, and then a quiz within that module.

    Args:
        quiz_directory (str): The path to the directory containing quiz themes.

    Returns:
        str: Path to the selected quiz file.
    """
    themes = list_themes(quiz_directory)
    selected_theme = st.selectbox("Select a Theme:", themes, key="unique_theme_select")

    if selected_theme:
        theme_directory = os.path.join(quiz_directory, selected_theme)
        modules = list_themes(theme_directory)

        if modules:
            selected_module = st.selectbox("Choose a Module:", modules, key="unique_module_select")

            if selected_module:
                module_directory = os.path.join(theme_directory, selected_module)
                quiz_files = list_quiz_files(module_directory)
                quiz_file_names = [os.path.splitext(f)[0] for f in quiz_files]  # Remove '.json' extension
                selected_quiz_name = st.selectbox("Choose a quiz:", quiz_file_names, key="unique_quiz_select")

                if selected_quiz_name:
                    selected_quiz = selected_quiz_name + '.json'  # Add '.json' extension back to find the file
                    return os.path.join(selected_theme, selected_module, selected_quiz)
        else:
            quiz_files = list_quiz_files(theme_directory)
            quiz_file_names = [os.path.splitext(f)[0] for f in quiz_files]  # Remove '.json' extension
            selected_quiz_name = st.selectbox("Choose a Quiz:", quiz_file_names, key="unique_quiz_select")

            if selected_quiz_name:
                selected_quiz = selected_quiz_name + '.json'  # Add '.json' extension back to find the file
                return os.path.join(selected_theme, selected_quiz)

    return None

# Displays quiz
def display_quiz(quiz_data):
    """
    Displays a quiz and collects user answers.

    Args:
        quiz_data (dict): The quiz data.

    Returns:
        dict: User answers where keys are question indices and values are lists of selected option indices.
    """
    # Extract quiz information
    title = quiz_data.get('quiz', {}).get('title', '')
    passingScore = quiz_data.get('quiz', {}).get('passingScore', None)
    congratulationsMessage = quiz_data.get('quiz', {}).get('congratulationsMessage', '')

    # Check if passingScore is found
    if passingScore is not None:
        st.markdown(f"<p style='color:green;'><strong>[GCP-Exam] Passing Score: {passingScore}%</strong></p>", unsafe_allow_html=True)
    else:
        pass  # Do nothing if passingScore is not found

    user_answers = {}
    for i, question in enumerate(quiz_data.get('quiz', {}).get('questions', [])):
        st.subheader(f"Question {i+1}:")
        st.write(question['questionText'])
        options = question['options']
        
        # Use st.checkbox for each option
        selected_options = [st.checkbox(option, key=f"q{i}_opt{j}") for j, option in enumerate(options)]
        
        # Store indices of selected options in a dictionary
        user_answers[i] = [j for j, selected in enumerate(selected_options) if selected]
    return user_answers



def reset_filter():
    """
    Resets the filter and state for user answers and checkbox states.
    """
    st.session_state.user_answers = []
    if 'checkbox_states' in st.session_state:
        st.session_state.checkbox_states.clear()
    st.session_state.timer_is_running = False
    st.session_state.timer_placeholder.empty()


#--------------#
# MAIN
#--------------#
def page_quiz():
    """
    Initializes and manages the display of a quiz within the Streamlit application.

    This function loads quiz data from a specified JSON file entered by the user,
    displays the selected quiz's questions, allows the user to answer the questions,
    and collects the user's answers.

    The user is prompted to enter the path to the JSON file containing the quiz data.
    Once the file is loaded, they can choose among several quizzes available in the same directory.
    After completing the quiz, the user's answers are returned for validation.
    """
    # st.subheader("🚀Quiz Session:")
    st.markdown("<h1 style='text-align: center;'>🚀Quiz Session</h1>", unsafe_allow_html=True)
    st.write("---")
    

    # Directory containing quiz files
    quiz_directory = "_quiz"

    # Select theme, module, and quiz
    selected_quiz_path = select_theme_module_and_quiz(quiz_directory)

    if selected_quiz_path:
        # Load the selected quiz file
        with open(os.path.join(quiz_directory, selected_quiz_path)) as f:
            quiz_data = json.load(f)

        if st.button("🔄 Reset Checkboxes"):
            reset_filter()

        # Display the quiz and collect user answers
        user_answers = display_quiz(quiz_data)
        return quiz_data, user_answers

    return None, None



