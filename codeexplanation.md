

---

# YouTube Video Summarizer with Flask

This README provides an overview of the code structure and functionality of the YouTube Video Summarizer with Flask application.

## Code Explanation

### Dependencies
- **Flask**: The web application framework used for handling HTTP requests and responses.
- **pytube**: Library for downloading YouTube videos.
- **moviepy**: Library for working with video files.
- **openai-python**: Python client for OpenAI API.
- **python-docx**: Library for creating and manipulating Word documents.

### Main Script (`app.py`)
- **Flask App Setup**: Initializes a Flask application.
- **Set Up OpenAI API Key**: Sets the OpenAI API key required for transcribing audio and generating summaries.
- **Extract Video ID**: Function to extract the video ID from a YouTube URL.
- **Download Video**: Function to download a YouTube video in the highest resolution available.
- **Transcribe Video**: Function to convert the downloaded video to an audio file and transcribe its contents using OpenAI's transcription API.
- **Summarize Text**: Function to summarize the transcribed text using OpenAI's GPT-3.5 Turbo model and save the summary in a Word document.
- **Run Program**: Function to coordinate the execution of the entire program, including downloading the video, transcribing it, and summarizing the transcript.
- **Flask Routes**:
  - **Index Route**: Displays the homepage with a form for submitting YouTube video URLs.
  - **Form Submission Route**: Handles form submissions, initiates the video summarization process, and redirects to the homepage.

### HTML Template (`index.html`)
- Provides the structure and layout for the web interface.
- Contains a form for submitting YouTube video URLs.

--- 
