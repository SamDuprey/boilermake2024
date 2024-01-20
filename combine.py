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

if __name__ == "__main__":
    video1 = "./assets/video.mov"  # Change the file extension to MOV
    video2 = "./assets/SubwaySurfers.mp4"  # Assuming this is the trimmed video with MOV format
    video2mov = "./assets/SubwaySurfers.mov"  # Change the file extension to MOV
    
    video2trimmed = "./assets/SubwaySurfers_Trimmed.mov"  # Trimmed video with MP4 format
    
    # convert_mp4_to_mov(video2, video2mov)  # Convert video1 to MOV format
    
    # trim_video_to_match_duration(video1, video2mov, video2trimmed)  # Trim video2 to match the duration of video1
    
    output_video = "./assets/combined.mov"  # Change the output file extension to MOV

    # # Combine trimmed video2 and video1
    combine_videos(video1, video2trimmed, output_video)
