--
# Technical Q&A with Audio Input - Streamlit Application

This is a Streamlit-based web application that presents users with random technical questions, allows them to record audio answers, transcribes the audio to text using speech recognition, and calculates the accuracy of their responses compared to predefined correct answers.

## Features
- Displays a random technical question from a predefined list.
- Records audio input (up to 20 seconds) via the user's microphone.
- Transcribes the audio to text using Google's Speech Recognition API.
- Calculates answer accuracy using the Levenshtein ratio.
- Provides feedback with the transcribed answer, accuracy percentage, and correct answer.

## Prerequisites
Before running the application, ensure you have the following installed on your system:
- **Python 3.7 or higher**: The programming language used to write the application.
- **A microphone**: Required for recording audio answers.
- **Internet connection**: Needed for Google's Speech Recognition API (optional if replaced with an offline model).

## Installation

### Step 1: Clone or Download the Code
Download the `app.py` file or clone this repository to your local machine.

### Step 2: Install Required Libraries
Open a terminal or command prompt and install the necessary Python libraries using `pip`. Run the following command:

```bash
pip install streamlit speechrecognition pyaudio levenshtein
```

#### Required Libraries
- **`streamlit`**: A Python framework for building interactive web applications.
- **`speechrecognition`**: A library for performing speech recognition, with support for various APIs (e.g., Google Speech Recognition).
- **`pyaudio`**: A library for handling audio input/output, required for microphone access in `speechrecognition`.
- **`levenshtein`**: A library for calculating the Levenshtein distance, used to measure the similarity between the user's answer and the correct answer.

### Step 3: Run the Application
1. Navigate to the directory containing `app.py` in your terminal:
   ```bash
   cd /path/to/your/directory
   ```
2. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided URL (usually `http://localhost:8501`) in your web browser.

## Usage
1. **Start the App**: Upon running, a random technical question will be displayed (e.g., "Question 1: What is the primary function of a CPU in a computer?").
2. **Record Your Answer**: Click the "Record Answer" button, speak your answer into the microphone (up to 20 seconds), and wait for the transcription.
3. **View Feedback**: The app will display your transcribed answer, accuracy percentage, and the correct answer.
4. **Next Question**: Click "Next Question" to get a new random question. The process repeats until all questions are used, then it resets.

## Technical Terms and Definitions
Below are definitions of key technical terms used in the code:

- **Streamlit**: An open-source Python framework for creating interactive, data-driven web applications with minimal code.
- **Speech Recognition**: The process of converting spoken language (audio) into text, implemented here using the `speechrecognition` library.
- **Levenshtein Ratio**: A measure of similarity between two strings, calculated as the ratio of matching characters to the total length, accounting for insertions, deletions, and substitutions. Used here to determine answer accuracy.
- **Microphone**: A hardware device that captures audio input, accessed via `pyaudio` in this app.
- **Session State**: A Streamlit feature (`st.session_state`) that persists data across user interactions, used here to track the current question, user answer, and accuracy.
- **Google Speech Recognition API**: A cloud-based service that transcribes audio to text, used as the default transcription method in this app (requires an internet connection).
- **Randomization**: The process of selecting items (questions) in an unpredictable order, implemented using Python's `random` module.
- **API (Application Programming Interface)**: A set of rules and tools that allows different software components to communicate, referenced in one of the questions.

## Notes
- **Internet Dependency**: The current implementation uses Google's free Speech Recognition API, which requires an internet connection. For offline use, replace it with an open-source model like `vosk` or `whisper` (additional setup required).
- **Accuracy Calculation**: The Levenshtein ratio is a simple string comparison method. It may not fully capture semantic accuracy (e.g., different wording with the same meaning). For advanced analysis, consider NLP models like BERT.
- **Microphone Access**: Ensure your system grants microphone permissions to the app. If issues arise, check your OS settings or `pyaudio` installation.

## Troubleshooting
- **"No module named X"**: Ensure all libraries are installed correctly with `pip install <library>`.
- **Microphone Errors**: Verify `pyaudio` is installed and your microphone is working. Test with a simple audio recording script if needed.
- **Blank Page**: Confirm Streamlit is running and access the correct URL (e.g., `http://localhost:8501`).

## Future Enhancements
- Replace Google’s API with an offline speech recognition model (e.g., `whisper`).
- Add a "Restart" button to reset the question sequence manually.
- Improve accuracy scoring with semantic analysis using NLP techniques.

---

This `README.md` provides a comprehensive guide for users to set up and understand the application, including technical definitions relevant to the code. Save it as `README.md` in the same directory as `app.py` for easy reference. Let me know if you'd like to refine it further!
