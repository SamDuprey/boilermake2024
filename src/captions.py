import os
import subprocess
import pyttsx3
from moviepy.editor import TextClip, concatenate_videoclips, CompositeVideoClip
from moviepy.editor import AudioFileClip
import re

language = 'en'

def remove_sentence_pauses(text):
    # Remove periods followed by a space to avoid pauses at the end of sentences
    return re.sub(r'\. ', '. ', text)

def create_audio(text, output_file):
    modified_text = remove_sentence_pauses(text)
    
    # Adjust the rate to set the speed (default is 200)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 20)  # Decrease the rate by 20 for a normal speed
    engine.save_to_file(modified_text, output_file)
    engine.runAndWait()
    
    return output_file

def generate_captions_video(text, output_file):
    # Convert text to speech using pyttsx3
    audio_file = create_audio(text, "temp_audio.wav")

    # Load the audio clip to get its duration
    audio_clip = AudioFileClip(audio_file)
    audio_duration = audio_clip.duration

    # Define video dimensions
    video_width, video_height = 406, 720  # You can adjust these dimensions

    # Split the text into words
    words = text.split()

    # Specify the number of words per caption
    words_per_caption = 3

    # Create a list to store TextClip instances
    text_clips = []

    # Create TextClip instances for each group of words
    for i in range(0, len(words), words_per_caption):
        caption_words = words[i:i + words_per_caption]
        caption_text = ' '.join(caption_words)

        # Check if the regular expression match is successful
        match = re.search(re.escape(caption_text), text)
        if match:
            # Extract start and end times from the match
            start_time = match.start() * audio_duration / len(text)
            end_time = match.end() * audio_duration / len(text)

            # Create TextClip for the caption with a green background
            text_clip = TextClip(caption_text, fontsize=30, color='white', bg_color='#00FF00', font='Helvetica-Neue-Bold', size=(video_width, video_height))

            # Set the duration and position of the text clip
            text_clip = text_clip.set_duration(end_time - start_time).set_position(('center', 'bottom')).set_start(start_time)

            # Append the text clip to the list
            text_clips.append(text_clip)

    # Concatenate the individual caption clips into a single video clip
    final_video = concatenate_videoclips(text_clips, method="compose")

    # Set the audio for the video clip
    final_video = final_video.set_audio(audio_clip)

    # Export the final video with synchronized audio in MOV format
    final_video.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24, remove_temp=True)

    # Remove temporary audio file
    os.remove(audio_file)

def fontlist():
  print(TextClip.list('font'))

