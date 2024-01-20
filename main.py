from google.cloud import texttospeech
from pydub import AudioSegment
from moviepy.editor import VideoClip, TextClip
from moviepy.editor.audio.AudioClip import AudioArrayClip

def generate_captioned_video(text_input, output_file):
    # Use Google Cloud Text-to-Speech to generate audio
    tts_client = texttospeech.TextToSpeechClient()
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

    # Save audio to file
    audio_file = "output_audio.wav"
    with open(audio_file, "wb") as out_audio:
        out_audio.write(response.audio_content)

    # Convert WAV audio to pydub AudioSegment
    audio = AudioSegment.from_wav(audio_file)

    # Create a simple video with captions using moviepy
    text_clip = TextClip(text=text_input, fontsize=20, color="white", bg_color="black")
    audio_clip = AudioArrayClip(audio.raw_data, fps=audio.frame_rate)
    video_clip = VideoClip([text_clip.set_audio(audio_clip)])

    # Synchronize audio and video
    audio_duration = len(audio) / 1000.0
    video_clip = video_clip.set_duration(audio_duration)

    # Export video to MP4
    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=audio.frame_rate)


def synthesize_text_with_api_key(api_key, text):
    client = texttospeech.TextToSpeechClient(api_key=api_key)

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open("output.wav", "wb") as out_audio:
        out_audio.write(response.audio_content)

# if __name__ == "__main__":
#     # Replace 'your_api_key' with the actual API key
#     api_key = 'your_api_key'
#     sample_text = "Hello, this is a sample text for text-to-speech."

#     synthesize_text_with_api_key(api_key, sample_text)


if __name__ == "__main__":
    input_text = "AITAH for divorcing my husband for a man who gave me a kidney? I (43F) have a genetic kidney condition and I lost the function of both of my kidneys a couple of years ago. I was on dialysis and on the transplant list. I never drank alcohol or did anything to exacerbate my disease. It’s just luck of the draw."
    output_video = "output_video.mp4"
    generate_captioned_video(input_text, output_video)
