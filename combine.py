import subprocess
from moviepy.editor import VideoFileClip

def trim_video_to_match_duration(video1, video2, output_video):
    # Load video clips
    clip1 = VideoFileClip(video1)
    clip2 = VideoFileClip(video2)

    # Trim the second video to match the duration of the first video
    trimmed_clip2 = clip2.subclip(0, clip1.duration)

    # Close the original video clips
    clip1.close()
    clip2.close()

    # Write the trimmed video to the output file
    trimmed_clip2.write_videofile(output_video, codec='libx264', audio_codec='aac', fps=24, remove_temp=False)



def combine_videos(input_video1, input_video2, output_video):
    # Run ffmpeg command to concatenate two videos
    cmd = [
        'ffmpeg',
        '-i', input_video1,
        '-i', input_video2,
        '-filter_complex', '[0:v][1:v]hstack=inputs=2[v];[0:a][1:a]amerge=inputs=2[a]',
        '-map', '[v]',
        '-map', '[a]',
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '192k',
        '-shortest',
        output_video
    ]

    subprocess.run(cmd)

# trim
if __name__ == "__main__":
    video1 = "video1.mp4"
    video2 = "video2.mp4"
    output_video = "trimmed_video2.mp4"

    trim_video_to_match_duration(video1, video2, output_video)
    
# combi
if __name__ == "__main__":
    input_video1 = "video1.mp4"
    input_video2 = "video2.mp4"
    output_video = "combined_video.mp4"

    combine_videos(input_video1, input_video2, output_video)
