import os

from src.captions import generate_captions_video
from src.combine import trim_video_to_match_duration, apply_chroma_key


def delete_pycache():
  os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')

def generate_video(text, background_video, output_file):
    captions_video_file =  "./assets/captions.mov"
    print("second parameter is " + str(background_video))
    # Extract the file name without extension from the background video path
    #background_video_name = os.path.splitext(os.path.basename(background_video))[0]
    background_video_name = background_video
    print("background_video_name" + background_video_name)

    # Use the extracted file name for the trimmed background video
    trimmed_background_video_file = "./assets/trimmed.mov"

    # generates video with tts and caption with green-screen background
    generate_captions_video(text, captions_video_file, "subway" in background_video_name)
    

    # trims the background video to be the same length as the caption
    trim_video_to_match_duration(captions_video_file, background_video_name, trimmed_background_video_file)
    
    # applys chroma key to remove the green background
    apply_chroma_key(trimmed_background_video_file, captions_video_file, output_file, similarity=0.3, blend=0.3)

# if __name__ == "__main__":
#     # text_to_speak = "AITAH for divorcing my husband for a man who gave me a kidney? I (43F) have a genetic kidney condition and I lost the function of both of my kidneys a couple of years ago. I was on dialysis and on the transplant list. I never drank alcohol or did anything to exacerbate my disease. It’s just luck of the draw."
#     # text_to_speak = "AITA for removing our family from our will We are a gay couple in our 50s. Decent amount of money and no kids. We do have 7 nieces and nephews. It has been assumed by both our families that our money would be split among them when we die. Not enough for them to retire but we are talking around 200,000 for each kid. "
#     # captions_video_file = "./assets/captions.mov"
#     # text_to_speak = "AITA for giving my child a vegan name? Hey Reddit, I need your judgment here. So, the other day, my partner (32M) and I (28F) welcomed our beautiful baby girl into the world. We were over the moon with joy and excitement, as any new parents would be."

#     text_to_speak = "Hey Reddit, I (30F) recently found myself in a tricky situation and need some perspective. My extended family is planning a big reunion, and everyone is excited about it. However, I have some personal boundaries that I've been trying to enforce for my mental well-being. Here's the deal: these family gatherings have always been chaotic, with lots of drama and unsolicited advice. Last time, it took me weeks to recover from the stress. So, this time around, I decided to prioritize my mental health and declined the invitation. Now, my family is upset with me, saying I'm being selfish and ruining the tradition. I understand the importance of family, but AITA for prioritizing my mental health and setting boundaries? I've tried explaining my reasons, but they don't seem to understand.I feel guilty for causing tension within the family, but I also believe it's essential to prioritize self-care. What do you think, Reddit? AITA for choosing my mental health over a family gathering, or should I have just sucked it up for the sake of tradition?"
#     # background_video_file = "./assets/SubwaySurfers.mov"
#     # trimmed_background_video_file = "./assets/SubwaySurfers_trimmed.mov"
    
#     # output_path = "./assets/output.mov"
    
#     # # generates video with tts and caption with green-screen background
#     # generate_captions_video(text_to_speak, captions_video_file)
    
#     # # deletes __pycache__ folder
#     # delete_pycache()
    
#     # # trims the background video to be the same length as the caption
#     # trim_video_to_match_duration(captions_video_file, background_video_file, trimmed_background_video_file)

#     # # applys chroma key to remove the green background
#     # apply_chroma_key(trimmed_background_video_file, captions_video_file, output_path, similarity=0.3, blend=0.3)
    
#     generate_video(text_to_speak, "./assets/SubwaySurfers.mov", "./assets/test_output.mov")
    


    
