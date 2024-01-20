# from google.cloud import texttospeech
# from pydub import AudioSegment
# from moviepy.editor import VideoClip, TextClip
# from moviepy.audio.io.AudioFileClip import AudioArrayClip

# def generate_captions(text_input, api_key):
#     tts_client = texttospeech.TextToSpeechClient(api_key=api_key)

#     synthesis_input = texttospeech.SynthesisInput(text=text_input)
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="en-US", name="en-US-Wavenet-D"
#     )
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.LINEAR16
#     )
#     response = tts_client.synthesize_speech(
#         input=synthesis_input, voice=voice, audio_config=audio_config
#     )

#     audio = AudioSegment.from_wav(AudioSegment.from_wav(response.audio_content))
#     return audio, text_input  # Return audio and text for synchronization

# def generate_captions_from_text(text_input):
#     # Replace this function with your existing code that generates captions
#     # For now, I'll just return the input text as a placeholder
#     return text_input

# def combine_and_sync(audio, captions, output_file):
#     # Create a simple video with captions using moviepy
#     text_clip = TextClip(text=captions, fontsize=20, color="white", bg_color="black")
#     audio_clip = AudioArrayClip(audio.raw_data, fps=audio.frame_rate)
#     video_clip = VideoClip([text_clip.set_audio(audio_clip)])

#     # Synchronize audio and video
#     audio_duration = len(audio) / 1000.0
#     video_clip = video_clip.set_duration(audio_duration)

#     # Export video to MP4
#     video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=audio.frame_rate)

# if __name__ == "__main__":
#     api_key = 'your_api_key'
#     sample_text = "Hello, this is a sample text for text-to-speech."

#     # Step 1: Generate captions using Text-to-Speech API
#     audio, text_for_sync = generate_captions(sample_text, api_key)

#     # Step 2: Generate captions from your existing code
#     captions = generate_captions_from_text(text_for_sync)

#     # Step 3: Combine and sync audio with captions
#     output_video = "output_video.mp4"
#     combine_and_sync(audio, captions, output_video)
from moviepy.config import change_settings
change_settings({"FFMPEG_BINARY": "/usr/bin/ffmpeg"})
from google.cloud import texttospeech
from pydub import AudioSegment
from moviepy.editor import VideoClip, TextClip
from moviepy.editor.audio.AudioClip import AudioArrayClip
import imageio_ffmpeg as ffmpeg  # Import imageio_ffmpeg to handle FFmpeg operations
import imageio

# Function to generate captions using the Text-to-Speech API
def generate_captions(text_input, api_key):
    tts_client = texttospeech.TextToSpeechClient(api_key=api_key)

    synthesis_input = texttospeech.SynthesisInput(text=text_input)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-D"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Corrected: Read audio content directly
    audio = AudioSegment.from_wav(io.BytesIO(response.audio_content))
    return audio, text_input  # Return audio and text for synchronization

# Function to generate captions from existing text (placeholder)
def generate_captions_from_text(text_input):
    # Replace this function with your existing code that generates captions
    # For now, I'll just return the input text as a placeholder
    return text_input

# Function to combine and sync audio with captions
def combine_and_sync(audio, captions, output_file):
    # Create a simple video with captions using moviepy
    text_clip = TextClip(text=captions, fontsize=20, color="white", bg_color="black")
    audio_clip = AudioArrayClip(audio.raw_data, fps=audio.frame_rate)
    video_clip = VideoClip([text_clip.set_audio(audio_clip)])

    # Synchronize audio and video
    audio_duration = len(audio) / 1000.0
    video_clip = video_clip.set_duration(audio_duration)

    # Set imageio_ffmpeg's FFmpeg executable path (change the path accordingly)
    imageio.plugins.ffmpeg.get_ffmpeg_version()

    # Export video to MP4
    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=audio.frame_rate)

if __name__ == "__main__":
    api_key = 'your_api_key'
    sample_text = "Hello, this is a sample text for text-to-speech."

    # Step 1: Generate captions using Text-to-Speech API
    audio, text_for_sync = generate_captions(sample_text, api_key)

    # Step 2: Generate captions from your existing code
    captions = generate_captions_from_text(text_for_sync)

    # Step 3: Combine and sync audio with captions
    output_video = "output_video.mp4"
    combine_and_sync(audio, captions, output_video)
