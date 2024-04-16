from flask import Flask, request, render_template
import os
import re
from pytube import YouTube
from moviepy.editor import VideoFileClip
import openai
import docx

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "Api key here"

# FUnction to extract URL
def extract_video_id(url):
    video_id = re.search(r'v=([^&]*)', url).group(1)
    return video_id

#Function to download The video 
def download_video(url):
    video_id = extract_video_id(url)
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=".", filename=f"{video_id}.mp4")
    print("Video downloaded successfully!")
    return os.path.abspath(os.path.join(os.getcwd(), f"{video_id}.mp4"))
# Functoin to to convert video to audio file and get the transcript
def transcribe_video(video_path):
    aud_file = os.path.join(os.getcwd(), "video.mp3")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(aud_file)

    try:
        # Open audio file
        audio_file = open(aud_file, "rb")

        # Transcribe audio file
        transcription = openai.Audio.transcribe("whisper-1", audio_file)

        # Print transcription
        print(transcription.text)

        # Save transcription to file
        with open("transcript.txt", "w") as f:
            f.write(transcription.text)

        print("Transcription successful!")
    except Exception as e:
        print(f"Failed to transcribe audio: {e}")

#Function to summarize the Transcript
def summarize_text_file_to_word(file_path):

    # Load the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Generate a summary using GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
        {"role": "user", "content": f"Summarize the following text: {text}"}
      ]
    )
    summary = response.choices[0].message.content

    # Create a new Word document
    doc = docx.Document()

    # Add the summary to the document
    doc.add_paragraph(summary)

    # Save the document as a Word file
    doc.save('summary.docx')

# Function to run the program
def run_program():
    url = request.form.get("url")
    video_path = download_video(url)
    transcribe_video(video_path)
    summarize_text_file_to_word(file_path)
#Website cration using flask
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        run_program()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)