import os

from captions import generate_captions_video
from combine import trim_video_to_match_duration, apply_chroma_key

def delete_pycache():
  os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')

def generate_video(text, background_video, output_file):
    captions_video_file =  "./assets/captions.mov"
    
    # Extract the file name without extension from the background video path
    background_video_name = os.path.splitext(os.path.basename(background_video))[0]

    # Use the extracted file name for the trimmed background video
    trimmed_background_video_file = f"./assets/{background_video_name}_trimmed.mov"

    # generates video with tts and caption with green-screen background
    generate_captions_video(text, captions_video_file)
    
    
    # trims the background video to be the same length as the caption
    trim_video_to_match_duration(captions_video_file, background_video, trimmed_background_video_file)
    
    # applys chroma key to remove the green background
    apply_chroma_key(trimmed_background_video_file, captions_video_file, output_file, similarity=0.3, blend=0.3)

if __name__ == "__main__":
    # text_to_speak = "AITAH for divorcing my husband for a man who gave me a kidney? I (43F) have a genetic kidney condition and I lost the function of both of my kidneys a couple of years ago. I was on dialysis and on the transplant list. I never drank alcohol or did anything to exacerbate my disease. It’s just luck of the draw."
    text_to_speak = "AITA for removing our family from our will We are a gay couple in our 50s. Decent amount of money and no kids. We do have 7 nieces and nephews. It has been assumed by both our families that our money would be split among them when we die. Not enough for them to retire but we are talking around 200,000 for each kid. "
    # captions_video_file = "./assets/captions.mov"
    # background_video_file = "./assets/SubwaySurfers.mov"
    # trimmed_background_video_file = "./assets/SubwaySurfers_trimmed.mov"
    
    # output_path = "./assets/output.mov"
    
    # # generates video with tts and caption with green-screen background
    # generate_captions_video(text_to_speak, captions_video_file)
    
    # # deletes __pycache__ folder
    # delete_pycache()
    
    # # trims the background video to be the same length as the caption
    # trim_video_to_match_duration(captions_video_file, background_video_file, trimmed_background_video_file)

    # # applys chroma key to remove the green background
    # apply_chroma_key(trimmed_background_video_file, captions_video_file, output_path, similarity=0.3, blend=0.3)
    
    generate_video(text_to_speak, "./assets/SubwaySurfers.mov", "./assets/test_output.mov")
    
 

    
