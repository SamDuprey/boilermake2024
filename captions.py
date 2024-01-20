import os
import pyttsx3
from moviepy.editor import TextClip, concatenate_videoclips
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
    video_width, video_height = 540, 960

    # Split the text into words
    words = text.split()

    # Specify the number of words per caption
    words_per_caption = 3

    # Create a list to store TextClip instances
    text_clips = []

    # Create TextClip instances for each group of words
    for i in range(0, len(words), words_per_caption):
        # Create a group of words for the caption
        caption_words = words[i:i + words_per_caption]

        # Join the words to form the caption text
        caption_text = ' '.join(caption_words)

        # Create TextClip for the caption
        text_clip = TextClip(caption_text, fontsize=24, color='white', bg_color='black', size=(video_width, video_height))

        # Find the corresponding TTS segment in the audio
        tts_segment_pattern = re.escape(' '.join(words[i:i + words_per_caption]))
        match = re.search(tts_segment_pattern, text)

        # Use the start and end times of the TTS segment
        start_time = match.start() * audio_duration / len(text)
        end_time = match.end() * audio_duration / len(text)

        # Set the duration and position of the text clip
        text_clip = text_clip.set_duration(end_time - start_time).set_position(('center', 'bottom')).set_start(start_time)

        # Append the text clip to the list
        text_clips.append(text_clip)

    # Concatenate the individual caption clips into a single video clip
    video_clip = concatenate_videoclips(text_clips, method="compose")

    # Set the audio for the video clip
    video_clip = video_clip.set_audio(audio_clip)

    # Export the final video with synchronized audio
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24, remove_temp=False)

    # Remove temporary audio and video file
    os.remove(audio_file)
    os.remove("videoTEMP_MPY_wvf_snd.mp4")  # Add this line to remove the temporary video file after running the script

if __name__ == "__main__":
    text_to_speak = "AITAH for divorcing my husband for a man who gave me a kidney? I (43F) have a genetic kidney condition and I lost the function of both of my kidneys a couple of years ago. I was on dialysis and on the transplant list. I never drank alcohol or did anything to exacerbate my disease. It’s just luck of the draw."
    output_video_file = "./assets/video.mp4"

    generate_captions_video(text_to_speak, output_video_file)
