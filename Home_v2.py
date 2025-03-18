import streamlit as st
import speech_recognition as sr
from Levenshtein import ratio
import random

# List of questions and answers
qa_pairs = [
    {"question": "What is the primary function of a CPU in a computer?", 
     "answer": "The Central Processing Unit (CPU) is the brain of a computer, responsible for executing instructions from programs by performing the basic operations of fetch, decode, and execute."},
    {"question": "How does a relational database differ from a non-relational database?", 
     "answer": "A relational database organizes data into structured tables with predefined schemas and relationships, while a non-relational database uses flexible, schema-less structures like key-value pairs, documents, or graphs, suited for unstructured data."},
    {"question": "What is the purpose of DNS in networking?", 
     "answer": "The Domain Name System (DNS) translates human-readable domain names into IP addresses that computers use to locate each other on the internet."},
    {"question": "What is the difference between HTTP and HTTPS?", 
     "answer": "HTTP is unsecured and transmits data in plain text, while HTTPS adds a layer of security using SSL/TLS encryption to protect data during transmission."},
    {"question": "What is the significance of Moore's Law?", 
     "answer": "Moore's Law predicts that the number of transistors on a microchip doubles approximately every two years, leading to exponential growth in computing power, though it’s now slowing due to physical limits."},
    {"question": "How does a hash function work in cryptography?", 
     "answer": "A hash function takes an input and produces a fixed-length string of characters, which is unique to the input. It’s one-way, meaning it’s computationally infeasible to reverse the hash to retrieve the original data."},
    {"question": "What is the role of an API in software development?", 
     "answer": "An Application Programming Interface (API) allows different software applications to communicate with each other by defining a set of rules and tools for requesting and exchanging data or functionality."},
    {"question": "What is the difference between RAM and ROM?", 
     "answer": "RAM is volatile, temporary storage used for running programs, while ROM is non-volatile, permanent storage for firmware or boot instructions that cannot be easily modified."},
    {"question": "How does a binary search algorithm work?", 
     "answer": "A binary search efficiently finds an element in a sorted array by repeatedly dividing the search range in half, comparing the middle element to the target, and narrowing the range until the target is found or determined to be absent."},
    {"question": "What is the purpose of a firewall in network security?", 
     "answer": "A firewall monitors and controls incoming and outgoing network traffic based on predefined security rules, acting as a barrier to prevent unauthorized access and cyberattacks."},
]

# Function to record and transcribe audio
def record_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Recording... Speak your answer now.")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=50)  # 20 seconds recording limit
        st.write("Recording complete. Processing...")
        try:
            text = recognizer.recognize_google(audio)  # Using Google's free API
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError:
            return "Error connecting to the speech recognition service."

# Function to calculate accuracy using Levenshtein ratio
def calculate_accuracy(user_answer, correct_answer):
    return ratio(user_answer.lower(), correct_answer.lower()) * 100

# Function to pick a random question
def get_random_question(used_questions):
    available_questions = [qa for idx, qa in enumerate(qa_pairs) if idx not in used_questions]
    if not available_questions:  # Reset if all questions have been used
        used_questions.clear()
        available_questions = qa_pairs
    return random.choice(available_questions)

# Streamlit app
def main():
    st.title("Technical Q&A with Audio Input")

    # Session state initialization
    if "used_questions" not in st.session_state:
        st.session_state.used_questions = set()  # Track used question indices
    if "current_qa" not in st.session_state:
        st.session_state.current_qa = get_random_question(st.session_state.used_questions)
        st.session_state.used_questions.add(qa_pairs.index(st.session_state.current_qa))
    if "user_answer" not in st.session_state:
        st.session_state.user_answer = None
    if "accuracy" not in st.session_state:
        st.session_state.accuracy = None
    if "show_correct_answer" not in st.session_state:
        st.session_state.show_correct_answer = False
    if "question_number" not in st.session_state:
        st.session_state.question_number = 1

    # Display current question
    st.write(f"**Question {st.session_state.question_number}:** {st.session_state.current_qa['question']}")

    # Record audio button
    if st.button("Record Answer"):
        st.session_state.user_answer = record_and_transcribe()
        if st.session_state.user_answer and "Sorry" not in st.session_state.user_answer and "Error" not in st.session_state.user_answer:
            st.session_state.accuracy = calculate_accuracy(st.session_state.user_answer, st.session_state.current_qa["answer"])
            st.session_state.show_correct_answer = True
        else:
            st.session_state.show_correct_answer = False

    # Display transcribed answer and accuracy
    if st.session_state.user_answer:
        st.write(f"**Your Answer:** {st.session_state.user_answer}")
        if st.session_state.accuracy is not None and st.session_state.show_correct_answer:
            st.write(f"**Accuracy:** {st.session_state.accuracy:.2f}%")
            st.write(f"**Correct Answer:** {st.session_state.current_qa['answer']}")
        elif "Sorry" in st.session_state.user_answer or "Error" in st.session_state.user_answer:
            st.write(st.session_state.user_answer)

    # Navigation button (only "Next" since we're randomizing)
    if st.button("Next Question"):
        st.session_state.current_qa = get_random_question(st.session_state.used_questions)
        st.session_state.used_questions.add(qa_pairs.index(st.session_state.current_qa))
        st.session_state.user_answer = None
        st.session_state.accuracy = None
        st.session_state.show_correct_answer = False
        st.session_state.question_number += 1

if __name__ == "__main__":
    main()
