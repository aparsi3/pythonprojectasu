# pythonprojectasu
MFG 598
Here's the README file for your Flask application:

---

# YouTube Video Summarizer with Flask

This Flask application allows you to input a YouTube video URL, download the video, transcribe its audio, summarize the transcript, and save the summary in a Word document.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- Required Python packages (`pytube`, `moviepy`, `openai-python`, `docx`)

You'll also need an OpenAI API key to transcribe the audio and generate the summary.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/your_repository.git
```

2. Install the required Python packages:

```bash
pip install flask pytube moviepy openai-python python-docx
```

## Usage

1. Set up your OpenAI API key by replacing `"API KEY HERE"` with your actual API key in the script.

2. Run the Flask application:

```bash
python app.py
```

3. Open your web browser and go to `http://127.0.0.1:5000/`.

4. Enter the URL of the YouTube video in the provided form and submit.

5. Wait for the application to download the video, transcribe its audio, summarize the transcript, and save the summary in a Word document.

## Important 
1.Make sure TO create the Api key for open Ai 
2.Make sure to add index.html file in the templates folder
3.Make sure you have given right path for storing all the data 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change

---
