import os
import subprocess

def convert_mp4_to_mov(input_mp4, output_mov):
    # Run ffmpeg command to convert MP4 to MOV
    cmd = [
        'ffmpeg',
        '-i', input_mp4,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '192k',
        output_mov
    ]

    subprocess.run(cmd)
    
def convert_mov_to_mp4(input_mov, output_mp4):
    # Run ffmpeg command to convert MOV to MP4
    cmd = [
        'ffmpeg',
        '-i', input_mov,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '192k',
        output_mp4
    ]

    subprocess.run(cmd, check=True)

def convert_mp3_to_wav(input_mp3, output_wav, delete_mp3=False):
    # Run ffmpeg command to convert MP3 to WAV with an option to delete
    cmd = [
        'ffmpeg',
        '-i', input_mp3,
        '-acodec', 'pcm_s16le',
        '-ar', '44100',
        output_wav
    ]

    subprocess.run(cmd)

    # Delete the MP3 file if specified
    if delete_mp3:
        os.remove(input_mp3)