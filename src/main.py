import os
from gtts import gTTS
from moviepy.editor import TextClip, CompositeVideoClip
from moviepy.editor import AudioFileClip
from textwrap import wrap

language = 'en'

def create_audio(text, output_file):
    output = gTTS(text=text, lang=language, slow=False, tld='com')
    output.save(output_file)
    return output_file

def generate_captions_video(text, output_file):
    # Convert text to speech using gTTS
    audio_file = create_audio(text, "temp_audio.mp3")

    # Load the audio clip to get its duration
    audio_clip = AudioFileClip(audio_file)
    audio_duration = audio_clip.duration

    # Define video dimensions and margin
    video_width, video_height = 540, 960
    margin = 20  # Adjust the margin size as needed

    # Split the text into lines
    lines = wrap(text, width=40)  # Adjust width based on your preference

    # Create a list to store TextClip instances
    text_clips = []

    # Create TextClip instances for each line
    for i, line in enumerate(lines):
        # Add margins to the text
        text_with_margin = f"\n{line}\n\n{lines[i+1] if i+1 < len(lines) else ''}"

        text_clip = TextClip(text_with_margin, fontsize=24, color='white', bg_color='black', size=(video_width, video_height))
        
        # Calculate the start and end times for each line
        line_duration = audio_duration / len(lines)
        start_time = i * line_duration
        end_time = (i + 1) * line_duration

        # Set the duration and position of the text clip
        text_clip = text_clip.set_duration(line_duration).set_position(('center', 'bottom')).set_start(start_time)

        # Append the text clip to the list
        text_clips.append(text_clip)

    # Create a CompositeVideoClip with the list of TextClip instances
    video_clip = CompositeVideoClip(text_clips)

    # Set the audio for the video clip
    video_clip = video_clip.set_audio(audio_clip)

    # Export the final video with synchronized audio
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24, remove_temp=False)

    # Remove temporary audio file
    os.remove(audio_file)

if __name__ == "__main__":
    text_to_speak = "AITAH for divorcing my husband for a man who gave me a kidney? I (43F) have a genetic kidney condition and I lost the function of both of my kidneys a couple of years ago. I was on dialysis and on the transplant list. I never drank alcohol or did anything to exacerbate my disease. It’s just luck of the draw."
    output_video_file = "video.mp4"

    generate_captions_video(text_to_speak, output_video_file)