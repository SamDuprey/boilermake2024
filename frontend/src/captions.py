import os
import subprocess
from pathlib import Path
from openai import OpenAI
from pathlib import Path
import shutil
from pydub import AudioSegment
from moviepy.editor import TextClip, concatenate_videoclips, CompositeVideoClip
from moviepy.editor import AudioFileClip
from src.convert import *
import re
import syllables
from decouple import config

language = 'en'

# gets the API key from the .env file
OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def count_syllables(word):
    return syllables.estimate(word)

def count_punctuation(text):
    commas_colons_semicolons = text.count(',') + text.count(':') + text.count(';') + text.count("–")
    periods_exclamation = text.count('.') 
    question = text.count('?') + text.count('!')

    return [commas_colons_semicolons, periods_exclamation, question]

def analyze_caption(caption_text):
    words = caption_text.split()

    syllables_count = {word: count_syllables(word) for word in words}

    total_syllables = sum(syllables_count.values())
    
    punctuation_counts = count_punctuation(caption_text)

    return .148 * total_syllables + .177 * punctuation_counts[0] + .209 * punctuation_counts[1] + .310 * punctuation_counts[2]


def create_audio(text, output_file):

    # Specify the file paths
    output_mp3 = Path(output_file).with_suffix('.mp3')

    # Generate speech using OpenAI API
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
        speed=1.3,
    )

    # Save the audio as MP3
    response.stream_to_file(output_mp3)

    output_wav = Path(output_file).with_suffix('.wav')
    
    convert_mp3_to_wav(output_mp3, output_wav, delete_mp3=True)
    
    # Return the output file path
    return str(output_wav)

def remove_sentence_pauses(text):
    # Remove periods followed by a space to avoid pauses at the end of sentences
    return re.sub(r'\. ', '. ', text)

def fontlist():
  print(TextClip.list('font'))

def audio_length(audio_file):
    # Get the duration of the audio file in seconds
    result = subprocess.run(['ffprobe', '-i', audio_file, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def generate_captions_video(text, output_file, subway):
    # Convert text to speech using pyttsx3
    audio_file = create_audio(text, "temp_audio.wav")

    # Load the audio clip to get its duration
    audio_clip = AudioFileClip(audio_file)
    audio_duration = audio_clip.duration
    video_width, video_height = 406, 720
    # Define video dimensions
    if (not subway):
        video_width = 608 # You can adjust these dimensions
        video_height = 1080

    # Split the text into words
    words = text.split()

    # Specify the number of words per caption
    words_per_caption = 3

    # Create a list to store TextClip instances
    text_clips = []
    start_time = 0
    # Create TextClip instances for each group of words
    for i in range(0, len(words), words_per_caption):
        caption_words = words[i:i + words_per_caption]
        caption_text = ' '.join(caption_words)
            # Extract start and end times from the match
        end_time = start_time + analyze_caption(caption_text)

        
        
        # Create TextClip for the caption with a green background
        #text_clip = TextClip(caption_text, fontsize=35, color='white', bg_color='#00FF00', font='Bangers', stroke_color='white', size=(video_width, video_height))
        text_clip = TextClip(caption_text, fontsize=35, color='white', bg_color='#00FF00', font='Arial Rounded MT Bold', stroke_color='black', size=(video_width, video_height))
            # Set the duration and position of the text clip
        text_clip = text_clip.set_duration(end_time - start_time).set_position(('center', 'bottom')).set_start(start_time)

            # Append the text clip to the list
        text_clips.append(text_clip)
            
            # Update the start time for the next caption
        start_time = end_time + .0001

    # Concatenate the individual caption clips into a single video clip
    final_video = concatenate_videoclips(text_clips, method="compose")

    # Set the audio for the video clip
    final_video = final_video.set_audio(audio_clip)

    # Export the final video with synchronized audio in MOV format
    final_video.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24, remove_temp=True, ffmpeg_params=['-y'])

    # Remove temporary audio file
    os.remove(audio_file)
  
    shutil.rmtree('./delete', ignore_errors=True)


