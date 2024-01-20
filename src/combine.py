import os
import subprocess
from moviepy.editor import VideoFileClip

def trim_video_to_match_duration(video1, video2, output_video):
    # Get the duration of video1
    duration_video1 = VideoFileClip(video1).duration
    
    # Run ffmpeg command to trim video2 to the duration of video1
    cmd = [
        'ffmpeg',
        '-i', video2,
        '-ss', '0',
        '-t', str(duration_video1),
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '192k',
        output_video
    ]

    subprocess.run(cmd)

def apply_chroma_key(subway_path, captions_path, output_path, similarity=0.1, blend=0.1):
    # Set the chroma key color (green in this case)
    chroma_key_color = "0x00FF00"  # Hex color code for green

    # Use ffmpeg to apply chroma keying
    cmd = [
        "ffmpeg",
        "-i", subway_path,
        "-i", captions_path,
        "-filter_complex", f"[1:v]colorkey={chroma_key_color}:{similarity}:{blend}[ckout];[0:v][ckout]overlay[out]",
        "-map", "[out]",
        "-map", "1:a",
        output_path
    ]

    subprocess.run(cmd, check=True)

def combine_videos(video1, video2, output_video):
    # Run ffmpeg command to overlay video1 onto video2 with audio
    cmd = [
        'ffmpeg',
        '-i', video2,              # Input background video (video2)
        '-i', video1,              # Input overlay video with audio (video1)
        '-filter_complex', '[1:v]scale=540:960 [ov]; [0:v][ov]overlay=0:0[v]; [1:a]adelay=delays=0|0 [a]',
        '-map', '[v]',
        '-map', '[a]',
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '192k',
        output_video
    ]

    subprocess.run(cmd)

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

