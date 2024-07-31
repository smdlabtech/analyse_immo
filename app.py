import streamlit as st
import os
import json
import latexifier
import time
import app_styles as app_styles
from _pages import home, topics, quiz, aboutme

### CONFIGURATIONS de la mise en page ###

# Check if page layout configuration is already set in st.session_state
if 'page_layout' not in st.session_state:
    st.session_state.page_layout = 'wide'  # Default layout

# Initial page configuration
st.set_page_config(
    page_title="Analyse Immo",
    page_icon="🏗️",
    layout=st.session_state.page_layout,
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': 'https://www.example.com/bug',
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Include Font Awesome once here (for adding icons and clickable links)
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

def display_html(file_name):
    """
    Displays HTML content from the specified file.

    Args:
        file_name (str): The name of the HTML file to display.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """
    try:
        html_content = app_styles.styles_html(file_name)
        st.markdown(html_content, unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Error: {e}")

def apply_css(file_name):
    """
    Applies CSS styles from the specified file.

    Args:
        file_name (str): The name of the CSS file to apply.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """
    try:
        css_content = app_styles.styles_css(file_name)
        st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
    except FileNotFoundError as e:
        st.error(f"Error: {e}")

@st.cache_data
def quiz_json(filepath):
    """
    Loads quiz data from a JSON file.

    Args:
        filepath (str): The relative path to the JSON file.

    Returns:
        dict: The quiz data.
    """
    quiz_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_quiz", filepath)
    with open(quiz_directory, 'r', encoding='utf-8') as file:
        quiz_data = json.load(file)
    return quiz_data

def go_to_previous_page():
    """
    Navigates to the previous page in the sequence.
    """
    pages = ["🏠Home", "📖Topics", "🚀Quiz", "😎AboutMe"]
    current_index = pages.index(st.session_state.page)
    if current_index > 0:
        st.session_state.page = pages[current_index - 1]

def go_to_next_page():
    """
    Navigates to the next page in the sequence.
    """
    pages = ["🏠Home", "📖Topics", "🚀Quiz", "😎AboutMe"]
    current_index = pages.index(st.session_state.page)
    if current_index < len(pages) - 1:
        st.session_state.page = pages[current_index + 1]

def start_timer(duration, timer_placeholder):
    """
    Starts a countdown timer.

    Args:
        duration (int): The duration of the timer in seconds.
        timer_placeholder (st.delta_generator.DeltaGenerator): The placeholder for displaying the timer.
    """
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time
        if remaining_time > 0:
            mins, secs = divmod(remaining_time, 60)
            timer_placeholder.markdown(f"### Time Remaining: {int(mins):02d}:{int(secs):02d}")
            time.sleep(1)
        else:
            timer_placeholder.markdown("### Time's up!")
            break

def reset_filter():
    """
    Resets the user answers and timer states.
    """
    st.session_state.user_answers = []
    if 'checkbox_states' in st.session_state:
        st.session_state.checkbox_states.clear()
    st.session_state.timer_is_running = False
    if 'timer_placeholder' in st.session_state:
        st.session_state.timer_placeholder.empty()

def validate_answers(quiz_data, user_answers):
    """
    Validates user answers against correct answers and calculates the score.

    Args:
        quiz_data (dict): The quiz data.
        user_answers (dict): User's answers where keys are question indices and values are lists of selected option indices.

    Returns:
        tuple: A tuple containing correct answers count, total questions count, and user's score.
    """
    correct_answers = 0
    total_questions = len(quiz_data['quiz']['questions'])

    for i, question in enumerate(quiz_data['quiz']['questions']):
        if i in user_answers:
            selected_option_index = user_answers[i]
            correct_option_index = question['answerIndex']
            if selected_option_index == correct_option_index:
                correct_answers += 1
                
    score = (correct_answers / total_questions) * 100
    return correct_answers, total_questions, score

def show_final_message(correct_answers, total_questions, score):
    """
    Displays the final message based on the quiz results.

    Args:
        correct_answers (int): Number of correct answers.
        total_questions (int): Total number of questions.
        score (float): User's score.
    """
    st.markdown("<span style='color: #f94a03;'>**Quiz finished!**</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #f94a03;'>You answered correctly to {correct_answers} questions out of {total_questions}.</span>", unsafe_allow_html=True)
    if score > 75:
        st.success(f"Congratulations! 😎\n\nYour score: {score:.2f}%.")
    elif score > 50:
        st.warning(f"Well done! 😉\n\nBut you can still do better.")
    else:
        st.error(f"Oops! 😧\n\nYour score: {score:.2f}% is insufficient!")

### MAIN ###
def main():
    """
    The main function to run the Streamlit app.
    """
    app_styles.load_css("body.css")
    
    # st.markdown("<h1 style='text-align: center;'>🏡Analyse Immo</h1>", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color = linear-gradient(to right, #243447, #08866F);'>🏗️Analyse Immo</h1>", unsafe_allow_html=True)
        # app_styles.styles_img("senlab_ia_gen_rmv_bgrd.png", caption="", width=10, use_column_width=True, output_format='PNG')
        # app_styles.styles_img("logo_immo (1).png", caption="🏛️Analyse Immo", width=10, use_column_width=True, output_format='PNG')
        app_styles.styles_img("logo_immo (2).png", caption="", width=10, use_column_width=True, output_format='PNG')
        st.sidebar.markdown("<h3 style='text-align: left; color: grey;'>Filters :</h3>", unsafe_allow_html=True)
        
        if "page" not in st.session_state:
            st.session_state.page = "🏠Home"

        page_size_option = st.sidebar.radio("Page size", ["Normal", "Wide"])

        if page_size_option == "Normal" and st.session_state.page_layout != "centered":
            st.session_state.page_layout = "centered"
            st.rerun()
        elif page_size_option == "Wide" and st.session_state.page_layout != "wide":
            st.session_state.page_layout = "wide"
            st.rerun()

        st.sidebar.button("🏠Home", on_click=lambda: st.session_state.update(page="🏠Home"))
        st.sidebar.button("📖Topics", on_click=lambda: st.session_state.update(page="📖Topics"))
        st.sidebar.button("🚀Quiz", on_click=lambda: st.session_state.update(page="🚀Quiz"))
        st.sidebar.button("😎AboutMe", on_click=lambda: st.session_state.update(page="😎AboutMe"))
        
    col1, col2, _ = st.columns([1, 8, 1])
    with col1:
        # if st.button("Prev."):
        if st.button("Prev."):
            go_to_previous_page()
    with col2:
        empty_space = st.empty()
    with _:
        # if st.button("Next"):
        if st.button("Next"):
            go_to_next_page()

    if st.session_state.page == "🏠Home":
        home.page_home()
    elif st.session_state.page == "📖Topics":
        topics.page_topics()
    elif st.session_state.page == "🚀Quiz":
        if 'timer_placeholder' not in st.session_state:
            st.session_state.timer_placeholder = st.empty()


        ##########################################
        # Quiz Answer Analysis
        quiz_data, user_answers = quiz.page_quiz()

        if quiz_data and user_answers:
            if st.button("Submit answers"):
                try:
                    correct_answers, total_questions, score = validate_answers(quiz_data, user_answers)
                    show_final_message(correct_answers, total_questions, score)

                    st.write("### Your Answers")
                    for i, question in enumerate(quiz_data['quiz']['questions']):
                        st.write(f"**Question {i+1}:** {question['questionText']}")
                        options = question['options']
                        selected_options = user_answers[i]

                        correct_count = 0
                        for j in selected_options:
                            if j in question['answerIndex']:
                                st.markdown(f"- {options[j]} ✔️")
                                correct_count += 1
                            else:
                                st.markdown(f"- <span style='color: #b11b03;'>{options[j]} ❌</span>", unsafe_allow_html=True)

                        if isinstance(question['answerIndex'], list):
                            correct_options = ", ".join([options[idx] for idx in question['answerIndex']])
                            st.markdown(f"<span style='color: green;'>**[{correct_count}/{len(selected_options)}] Correct answer(s)**: {correct_options}</span>", unsafe_allow_html=True)

                            if 'explanation' in question and len(question['explanation']) > 0:
                                st.markdown(f"<span style='color: green;'> **Why?** : {question['explanation']}</span>", unsafe_allow_html=True)

                            if 'validationQuery' in question and len(question['validationQuery']) > 0:
                                st.markdown(f"<span style='color: grey;'> **More details [BigQuery SQL]** : {question['validationQuery']}</span>", unsafe_allow_html=True)

                            if 'validationCommand' in question and len(question['validationCommand']) > 0:
                                st.markdown(f"<span style='color: grey;'> **More details [gcloud]** : {question['validationCommand']}</span>", unsafe_allow_html=True)

                            if 'Feedback' in question and question['Feedback']:
                                st.markdown("<span style='color: grey;'>**Feedback**:</span>", unsafe_allow_html=True)
                                for index, feedback in enumerate(question['Feedback'], start=1):
                                    st.markdown(f"<p><span style='color: grey;'>{feedback}</span></p>", unsafe_allow_html=True)

                            if 'links' in question and question['links']:
                                st.markdown("<span style='color: grey;'>**Links**:</span>", unsafe_allow_html=True)
                                for index, link in enumerate(question['links'], start=1):
                                    st.markdown(f"<p><span style='color: grey;'>{index}. <a href='{link}' target='_blank'>{link}</a></span></p>", unsafe_allow_html=True)

                        else:
                            st.markdown(f"<span style='color: green;'>**[{correct_count}/{len(selected_options)}] Correct answer(s)**: {correct_options}</span>", unsafe_allow_html=True)

                except TypeError:
                    st.error("Error: An unexpected error occurred while processing your quiz answers.")

    elif st.session_state.page == "😎AboutMe":
        aboutme.page_aboutme()
            
    display_html("footer.html")
    with st.sidebar:
        display_html("footer.html")


#------------------------#
#   Main App Function    #
#------------------------#
if __name__ == "__main__":
    main()
